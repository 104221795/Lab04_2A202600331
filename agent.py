import os
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_google_genai import ChatGoogleGenerativeAI # Sử dụng Gemini 2.5 Flash-Lite của bạn
from langchain_core.messages import SystemMessage
from tools import search_flights, search_hotels, calculate_budget # Import từ file tools.py đã viết
from dotenv import load_dotenv

# Load biến môi trường từ .env
load_dotenv()

# 1. Đọc System Prompt từ file đã tạo ở Phần 1
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# 2. Khai báo State (Trạng thái của Agent)
class AgentState(TypedDict):
    # add_messages giúp cộng dồn lịch sử chat thay vì ghi đè
    messages: Annotated[list, add_messages]

# 3. Khởi tạo LLM và Tools
tools_list = [search_flights, search_hotels, calculate_budget]
# Thay thế gpt-4o-mini bằng Gemini 2.5 Flash-Lite 
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite", 
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)
llm_with_tools = llm.bind_tools(tools_list)

# 4. Định nghĩa Agent Node
def agent_node(state: AgentState):
    messages = state["messages"]
    
    # Nếu tin nhắn đầu tiên chưa phải là SystemMessage, hãy chèn vào
    if not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages
    
    response = llm_with_tools.invoke(messages)
    
    # LOGGING: Để bạn theo dõi Agent đang gọi tool gì (theo yêu cầu hình 3fabfd)
    if response.tool_calls:
        for tc in response.tool_calls:
            print(f"--- 🛠️ Gọi tool: {tc['name']}({tc['args']}) ---")
    else:
        print("--- 💬 Trả lời trực tiếp ---")
        
    return {"messages": [response]}

# 5. Xây dựng Graph (Luồng xử lý)
builder = StateGraph(AgentState)

# Thêm các Node
builder.add_node("agent", agent_node)
tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)

# --- TODO: Khai báo Edges (Hoàn thiện theo yêu cầu bài Lab) ---
# Bắt đầu từ START sẽ vào node agent
builder.add_edge(START, "agent")

# Sau khi agent xử lý, sử dụng tools_condition để quyết định:
# - Nếu agent muốn gọi tool -> chuyển sang node "tools"
# - Nếu agent đã trả lời xong -> kết thúc (END)
builder.add_conditional_edges("agent", tools_condition)

# Sau khi thực hiện tool xong, phải quay lại node agent để LLM đọc kết quả tool
builder.add_edge("tools", "agent")

# Compile Graph
graph = builder.compile()

# 6. Chat loop (Vòng lặp tương tác)
if __name__ == "__main__":
    print("=" * 60)
    print("TravelBuddy - Trợ lý Du lịch Thông minh (Gemini 2.5 Flash-Lite)")
    print("         Gõ 'quit', 'exit' hoặc 'q' để thoát")
    print("=" * 60)

    while True:
        user_input = input("\nBạn: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("TravelBuddy: Tạm biệt! Chúc bạn có những chuyến đi thú vị.")
            break

        print("\nTravelBuddy đang suy nghĩ...")
        
        # Invoke graph với input của người dùng
        # Chú ý: Đầu vào là một list các message
        result = graph.invoke({"messages": [("user", user_input)]})
        
        # Lấy tin nhắn cuối cùng (phản hồi của Agent) để hiển thị
        final_response = result["messages"][-1]
        print(f"\nTravelBuddy: {final_response.content}")