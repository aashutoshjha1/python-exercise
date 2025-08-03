#!/usr/bin/env python3

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>FastAPI Example</title>
        </head>
        <body>
            <h1>Welcome to FastAPI!</h1>
            <p>This is a simple example of a FastAPI application.</p>
        </body>
    </html>
    """
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}
@app.get("/subtract/{a}/{b}")
def subtract(a: int, b: int):
    return {"result": a - b}
@app.get("/multiply/{a}/{b}")
def multiply(a: int, b: int):
    return {"result": a * b}
@app.get("/divide/{a}/{b}") 
def divide(a: int, b: int):
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": a / b}
@app.get("/power/{base}/{exponent}")
def power(base: int, exponent: int):
    return {"result": base ** exponent}
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    items = [{"item_id": i} for i in range(skip, skip + limit)]
    return {"items": items}
@app.get("/items/{item_id}/details")
def read_item_details(item_id: int, detail: str = None):
    return {"item_id": item_id, "detail": detail}
@app.get("/items/{item_id}/price")      
def read_item_price(item_id: int, currency: str = "USD"):
    price = 100.0
    if currency == "EUR":
        price *= 0.85
    elif currency == "GBP":
        price *= 0.75
    return {"item_id": item_id, "price": price, "currency": currency}
@app.get("/items/{item_id}/stock")
def read_item_stock(item_id: int, in_stock: bool = True):
    return {"item_id": item_id, "in_stock": in_stock}
@app.get("/items/{item_id}/reviews")
def read_item_reviews(item_id: int, rating: int = 5):
    reviews = [{"item_id": item_id, "rating": rating, "review": "Great item!"}]
    return {"item_id": item_id, "reviews": reviews}
@app.get("/items/{item_id}/related")
def read_related_items(item_id: int, category: str = None):
    related_items = [{"item_id": item_id + i, "category": category} for i in range(3)]
    return {"item_id": item_id, "related_items": related_items}
@app.get("/items/{item_id}/history")        
def read_item_history(item_id: int, days: int = 30):
    history = [{"item_id": item_id, "days": days, "action": "viewed"}]
    return {"item_id": item_id, "history": history}
@app.get("/items/{item_id}/similar")
def read_similar_items(item_id: int, similarity_score: float = 0.9):
    similar_items = [{"item_id": item_id + i, "similarity_score": similarity_score} for i in range(3)]
    return {"item_id": item_id, "similar_items": similar_items}
@app.get("/items/{item_id}/recommendations")
def read_recommendations(item_id: int, user_id: int = 1):
    recommendations = [{"item_id": item_id + i, "user_id": user_id} for i in range(3)]
    return {"item_id": item_id, "recommendations": recommendations}
@app.get("/items/{item_id}/availability")
def read_item_availability(item_id: int, location: str = "US"):
    availability = {"item_id": item_id, "available": True, "location": location}
    return availability
@app.get("/items/{item_id}/discount")
def read_item_discount(item_id: int, discount_code: str = None):
    discount = 0.1 if discount_code else 0.0
    return {"item_id": item_id, "discount": discount, "final_price": 100 * (1 - discount)}
@app.get("/items/{item_id}/warranty")       
def read_item_warranty(item_id: int, warranty_years: int = 1):
    warranty_info = {"item_id": item_id, "warranty_years": warranty_years, "warranty_valid": True}
    return warranty_info
@app.get("/items/{item_id}/shipping")
def read_item_shipping(item_id: int, shipping_method: str = "standard"):
    shipping_info = {"item_id": item_id, "shipping_method": shipping_method, "estimated_delivery": "5-7 days"}
    return shipping_info
@app.get("/items/{item_id}/return_policy")              
def read_item_return_policy(item_id: int, return_period: int = 30):
    return_policy = {"item_id": item_id, "return_period": return_period, "returnable": True}
    return return_policy
@app.get("/items/{item_id}/support")
def read_item_support(item_id: int, support_level: str = "standard"):
    support_info = {"item_id": item_id, "support_level": support_level, "support_available": True}
    return support_info
@app.get("/items/{item_id}/details/{detail_id}")
def read_item_detail(item_id: int, detail_id: int):
    return {"item_id": item_id, "detail_id": detail_id, "detail": "Detail information"}
@app.get("/items/{item_id}/specs")
def read_item_specs(item_id: int, spec_type: str = "default"):
    specs = {"item_id": item_id, "spec_type": spec_type, "specs": {"weight": "1kg", "color": "red"}}
    return specs
@app.get("/items/{item_id}/images")
def read_item_images(item_id: int, image_type: str = "thumbnail"):
    images = [{"item_id": item_id, "image_type": image_type, "url": f"http://example.com/image_{i}.jpg"} for i in range(3)]
    return {"item_id": item_id, "images": images}
@app.get("/items/{item_id}/videos")
def read_item_videos(item_id: int, video_quality: str = "720p"):
    videos = [{"item_id": item_id, "video_quality": video_quality, "url": f"http://example.com/video_{i}.mp4"} for i in range(2)]
    return {"item_id": item_id, "videos": videos}
@app.get("/items/{item_id}/faq")
def read_item_faq(item_id: int, question: str = None):
    faq = [{"item_id": item_id, "question": question or "What is this item?", "answer": "This is a great item."}]
    return {"item_id": item_id, "faq": faq}
@app.get("/items/{item_id}/related/{related_id}")
def read_related_item(item_id: int, related_id: int):
    return {"item_id": item_id, "related_id": related_id, "related_item": "Related item information"}
@app.get("/items/{item_id}/reviews/{review_id}")
def read_item_review(item_id: int, review_id: int):
    return {"item_id": item_id, "review_id": review_id, "review": "This is a great item!"}
@app.get("/items/{item_id}/stock/{location}")               
def read_item_stock_location(item_id: int, location: str):
    stock_info = {"item_id": item_id, "location": location, "in_stock": True}
    return stock_info
@app.get("/items/{item_id}/history/{history_id}")   
def read_item_history_id(item_id: int, history_id: int):
    return {"item_id": item_id, "history_id": history_id, "history": "Item history information"}
@app.get("/items/{item_id}/similar/{similar_id}")
def read_similar_item(item_id: int, similar_id: int):
    return {"item_id": item_id, "similar_id": similar_id, "similar_item": "Similar item information"}
@app.get("/items/{item_id}/recommendations/{recommendation_id}")
def read_recommendation(item_id: int, recommendation_id: int):
    return {"item_id": item_id, "recommendation_id": recommendation_id, "recommendation": "Recommended item information"}
@app.get("/items/{item_id}/availability/{location}")
def read_item_availability_location(item_id: int, location: str):
    availability = {"item_id": item_id, "location": location, "available": True}
    return availability
@app.get("/items/{item_id}/discount/{discount_code}")
def read_item_discount_code(item_id: int, discount_code: str):
    discount = 0.1 if discount_code else 0.0
    return {"item_id": item_id, "discount_code": discount_code, "final_price": 100 * (1 - discount)}
@app.get("/items/{item_id}/warranty/{warranty_years}")
def read_item_warranty_years(item_id: int, warranty_years: int):
    warranty_info = {"item_id": item_id, "warranty_years": warranty_years, "warranty_valid": True}
    return warranty_info
@app.get("/items/{item_id}/shipping/{shipping_method}")
def read_item_shipping_method(item_id: int, shipping_method: str):
    shipping_info = {"item_id": item_id, "shipping_method": shipping_method, "estimated_delivery": "5-7 days"}
    return shipping_info
@app.get("/items/{item_id}/return_policy/{return_period}")
def read_item_return_policy_period(item_id: int, return_period: int):
    return_policy = {"item_id": item_id, "return_period": return_period, "returnable": True}
    return return_policy
@app.get("/items/{item_id}/support/{support_level}")
def read_item_support_level(item_id: int, support_level: str):
    support_info = {"item_id": item_id, "support_level": support_level, "support_available": True}
    return support_info     
@app.get("/items/{item_id}/details/{detail_id}/specs")
def read_item_detail_specs(item_id: int, detail_id: int, spec_type: str = "default"):
    specs = {"item_id": item_id, "detail_id": detail_id, "spec_type": spec_type, "specs": {"weight": "1kg", "color": "red"}}
    return specs
@app.get("/items/{item_id}/images/{image_type}")
def read_item_image_type(item_id: int, image_type: str = "thumbnail"):
    images = [{"item_id": item_id, "image_type": image_type, "url": f"http://example.com/image_{i}.jpg"} for i in range(3)]
    return {"item_id": item_id, "images": images}
@app.get("/items/{item_id}/videos/{video_quality}")
def read_item_video_quality(item_id: int, video_quality: str = "720p"):
    videos = [{"item_id": item_id, "video_quality": video_quality, "url": f"http://example.com/video_{i}.mp4"} for i in range(2)]
    return {"item_id": item_id, "videos": videos}
@app.get("/items/{item_id}/faq/{question}")
def read_item_faq_question(item_id: int, question: str = None):
    faq = [{"item_id": item_id, "question": question or "What is this item?", "answer": "This is a great item."}]
    return {"item_id": item_id, "faq": faq}
@app.get("/items/{item_id}/related/{related_id}/details")
def read_related_item_details(item_id: int, related_id: int):
    return {"item_id": item_id, "related_id": related_id, "related_item": "Related item information with details"}
@app.get("/items/{item_id}/reviews/{review_id}/details")
def read_item_review_details(item_id: int, review_id: int):
    return {"item_id": item_id, "review_id": review_id, "review": "This is a great item with detailed review!"}
@app.get("/items/{item_id}/stock/{location}/details")
def read_item_stock_location_details(item_id: int, location: str):
    stock_info = {"item_id": item_id, "location": location, "in_stock": True, "details": "Stock information details"}
    return stock_info
@app.get("/items/{item_id}/history/{history_id}/details")
def read_item_history_id_details(item_id: int, history_id: int):
    return {"item_id": item_id, "history_id": history_id, "history": "Item history information with details"}
@app.get("/items/{item_id}/similar/{similar_id}/details")
def read_similar_item_details(item_id: int, similar_id: int):
    return {"item_id": item_id, "similar_id": similar_id, "similar_item": "Similar item information with details"}          
@app.get("/items/{item_id}/recommendations/{recommendation_id}/details")
def read_recommendation_details(item_id: int, recommendation_id: int):
    return {"item_id": item_id, "recommendation_id": recommendation_id, "recommendation": "Recommended item information with details"}
@app.get("/items/{item_id}/availability/{location}/details")
def read_item_availability_location_details(item_id: int, location: str):
    availability = {"item_id": item_id, "location": location, "available": True, "details": "Availability information details"}
    return availability         