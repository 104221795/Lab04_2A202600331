>>Giới thiệu
>Project này xây dựng một trợ lý du lịch thông minh sử dụng framework LangGraph kết hợp với mô hình Gemini 2.5 Flash-Lite. Agent có khả năng tự động suy luận, sử dụng công cụ (tool calling) để tra cứu thông tin và quản lý ngân sách chuyến đi cho người dùng.

>>Cấu trúc thư mục
>Dưới đây là chi tiết các file trong project:

- agent.py: File thực thi chính. Chứa định nghĩa về đồ thị trạng thái (StateGraph), các nút (Nodes) và các cạnh (Edges). Đây là nơi điều khiển luồng suy nghĩ của Agent.

- tools.py: Chứa 3 công cụ chính mà Agent có thể sử dụng:

- search_flights: Tra cứu vé máy bay (hỗ trợ tra cứu đảo ngược hành trình).

- Google Hotels: Tìm khách sạn (có lọc theo giá và sắp xếp theo rating).

- calculate_budget: Tính toán chi phí thực tế và kiểm tra giới hạn ngân sách.

- system_prompt.txt: Định nghĩa Persona (Cá tính), Rules (Quy tắc) và Constraints (Ràng buộc) cho Agent bằng cấu trúc XML.

- system_prompt_explaination.txt: Giải thích cho sự cải tiến, add prompt

- test_api.py: Ping API 

- test_results.md để đưa ra log một cách chân thật nhất đáp ứng đầy đủ 5 test cases 
