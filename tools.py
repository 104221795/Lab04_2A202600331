from langchain_core.tools import tool

# =========================================================
# Đây là Dữ liệu giả lập hệ thống du lịch từ Lab 4
# =========================================================

FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1_450_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2_800_000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1_200_000, "class": "economy"},
        
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1_350_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1_100_000, "class": "economy"},
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1_600_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1_300_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3_200_000, "class": "business"},
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1_300_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780_000, "class": "economy"},
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650_000, "class": "economy"},
    ]
}

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1_800_000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1_200_000, "area": "Mỹ Khê", "rating": 4.3},
        {"name": "Fivitel Danang", "stars": 3, "price_per_night": 650_000, "area": "Sơn Trà", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250_000, "area": "Hải Châu", "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 2, "price_per_night": 350_000, "area": "An Thượng", "rating": 4.7},
    ],
    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3_500_000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1_500_000, "area": "Bãi Trường", "rating": 4.2},
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800_000, "area": "Dương Đông", "rating": 4.0},
        {"name": "9Station Hostel", "stars": 2, "price_per_night": 200_000, "area": "Dương Đông", "rating": 4.5},
    ],
    "Hồ Chí Minh": [
        {"name": "Rex Hotel", "stars": 5, "price_per_night": 2_800_000, "area": "Quận 1", "rating": 4.3},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1_400_000, "area": "Quận 1", "rating": 4.1},
        {"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550_000, "area": "Quận 3", "rating": 4.4},
        {"name": "The Common Room", "stars": 2, "price_per_night": 180_000, "area": "Quận 1", "rating": 4.6},
    ]
}

# =========================================================
# TOOL DEFINITIONS
# =========================================================

def format_currency(amount: int) -> str:
    """Helper to format numbers to 1.450.000đ"""
    return f"{amount:,}".replace(",", ".") + "đ"
#Format tiền để có thể ra được giá tiền thêm giá trị việt nam đồng để format câu hỏi
@tool
def search_flights(origin: str, destination: str) -> str:
    #định dạng chỗ ở chỗ đến
    """
    Tìm kiếm các chuyến bay giữa hai thành phố.
    Tham số:
    - origin: thành phố khởi hành (VD: 'Hà Nội')
    - destination: thành phố đến (VD: 'Đà Nẵng')
    """
    # Thử tra cứu theo chiều thuận
    flights = FLIGHTS_DB.get((origin, destination))
    
    # Nếu không thấy, thử tra ngược chiều (Yêu cầu hình 4)
    if not flights:
        flights = FLIGHTS_DB.get((destination, origin))
        if flights:
            origin, destination = destination, origin # Đảo lại tên để hiển thị đúng

    if not flights:
        return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."

    result = f"Danh sách chuyến bay từ {origin} đến {destination}:\n"
    for f in flights:
        price_str = format_currency(f['price'])
        result += f"- {f['airline']} ({f['class']}): {f['departure']} -> {f['arrival']} | Giá: {price_str}\n"
    return result

@tool
def search_hotels(city: str, max_price_per_night: int = 99999999) -> str:
    """
    Tìm kiếm khách sạn tại một thành phố, có thể lọc theo giá tối đa mỗi đêm.
    """
    hotels = HOTELS_DB.get(city, [])
    
    # Lọc theo giá và Sắp xếp theo rating giảm dần (Yêu cầu hình 2 & 4)
    filtered_hotels = [h for h in hotels if h['price_per_night'] <= max_price_per_night]
    filtered_hotels.sort(key=lambda x: x['rating'], reverse=True)

    if not filtered_hotels:
        return f"Không tìm thấy khách sạn tại {city} với giá dưới {format_currency(max_price_per_night)}/đêm. Hãy thử tăng ngân sách."

    result = f"Khách sạn tại {city} (Sắp xếp theo đánh giá tốt nhất):\n"
    for h in filtered_hotels:
        price_str = format_currency(h['price_per_night'])
        result += f"- {h['name']} ({h['stars']} sao) - {h['area']}: {price_str}/đêm | Rating: {h['rating']}\n"
    return result

@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Tính toán ngân sách còn lại sau khi trừ các khoản chi phí thu chi.
    expenses: định dạng 'tên_khoản:số_tiền,tên_khoản:số_tiền'
    """
    try:
        # Parse chuỗi expenses thành dict (Yêu cầu hình 3)
        expense_dict = {}
        items = expenses.split(",")
        for item in items:
            name, amount = item.split(":")
            expense_dict[name.strip()] = int(amount.strip())
        
        total_spent = sum(expense_dict.values())
        remaining = total_budget - total_spent
        
        # Format bảng chi tiết
        result = "Bảng chi phí:\n"
        for name, amount in expense_dict.items():
            result += f"- {name.replace('_', ' ').capitalize()}: {format_currency(amount)}\n"
        
        result += "---\n"
        result += f"Tổng chi: {format_currency(total_spent)}\n"
        result += f"Ngân sách: {format_currency(total_budget)}\n"
        result += f"Còn lại: {format_currency(remaining)}\n"
        
        if remaining < 0:
            result += f"⚠️ Vượt ngân sách cho phép {format_currency(abs(remaining))}! Cần điều chỉnh."
            
        return result
    except Exception:
        return "Lỗi: Định dạng expenses sai. Vui lòng dùng 'tên:số_tiền,tên:số_tiền' (VD: 've_may_bay:1000000')."
    
    #Định dạng đúng ngân sách, xử lí lỗi sử dụng hàm try/except 