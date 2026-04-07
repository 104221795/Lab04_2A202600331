
# =========================================================
>> Test 1: Direct Answer (No tool Needed)
# =========================================================
Bạn: tôi muôn đi du lich 

TravelBuddy đang suy nghĩ...
--- 💬 Trả lời trực tiếp ---

TravelBuddy: Tuyệt vời! Bạn muốn đi đâu và khi nào thế? Cho mình biết ngân sách dự kiến của bạn nữa nhé, để mình dễ dàng lên kế hoạch cho bạn nè. 😊

Bạn: xin chao ! Tôi muôn đi du lich nhưng chưa biêt đi đâu

TravelBuddy đang suy nghĩ...
--- 💬 Trả lời trực tiếp ---

TravelBuddy: Chào bạn! Để mình giúp bạn lên kế hoạch cho chuyến đi nhé. Bạn thích đi biển, núi hay khám phá thành phố? Và bạn dự định đi bao nhiêu ngày, ngân sách của bạn khoảng bao nhiêu nhỉ? Cho mình biết thêm thông tin để mình tư vấn điểm đến phù hợp nha! 😊


# =========================================================
>>Test 2 - Single Tool Call
# =========================================================

Bạn: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng 
TravelBuddy đang suy nghĩ...
--- 🛠️ Gọi tool: search_flights({'destination': 'Đà Nẵng', 'origin': 'Hà Nội'}) ---
--- 💬 Trả lời trực tiếp ---

TravelBuddy: Chào bạn, mình tìm được một số chuyến bay từ Hà Nội đi Đà Nẵng như sau:
- Vietnam Airlines (economy): 06:00 -> 07:20 | Giá: 1.450.000đ
- Vietnam Airlines (business): 14:00 -> 15:20 | Giá: 2.800.000đ
- VietJet Air (economy): 08:30 -> 09:50 | Giá: 890.000đ
- Bamboo Airways (economy): 11:00 -> 12:20 | Giá: 1.200.000đ

# =========================================================
>>Test 3 - Multi_step Tool Chaining 
# =========================================================
 
Bạn: toi o Ha Noi muon di Phu Quoc 2 dem, budget 5 trieu. Tu van giup toi

TravelBuddy đang suy nghĩ...
--- 💬 Trả lời trực tiếp ---

TravelBuddy: Chào bạn, mình là trợ lý du lịch của TravelBuddy đây! Phú Quốc 2N1Đ với budget 5 triệu thì mình lo được hết nha. Để mình check vé máy bay và khách sạn cho bạn liền nè.

Bạn cho mình xin ngày đi cụ thể để mình tìm vé với khách sạn cho chuẩn nha!


# =========================================================
>>Test 4 - Missing Info/Clarification  
# =========================================================
Bạn: Tôi muôn đăt khach san

TravelBuddy đang suy nghĩ...
--- 💬 Trả lời trực tiếp ---

TravelBuddy: Ok bạn ơi, bạn muốn đặt khách sạn ở đâu và ngân sách cho khách sạn là bao nhiêu nè? Cho mình biết thêm thông tin để mình tìm giúp bạn nha! 😊



# =========================================================
>> Test 5 - Guardrail / Refusal  
# =========================================================
Bạn: giai giup toi bai tap toan 

TravelBuddy đang suy nghĩ...
--- 💬 Trả lời trực tiếp ---

TravelBuddy: Xin lỗi bạn, mình chỉ có thể giúp bạn về các vấn đề du lịch thôi. Bạn có cần mình tìm tour hay khách sạn ở đâu không?
Bạn: Giải giúp tôi bài tập lập trình Python về linked list

TravelBuddy đang suy nghĩ...
--- 💬 Trả lời trực tiếp ---

TravelBuddy: Xin lỗi bạn, mình chỉ có thể giúp bạn về các vấn đề liên quan đến du lịch thôi. Bạn có cần mình tìm vé máy bay hay khách sạn cho chuyến đi sắp tới không?