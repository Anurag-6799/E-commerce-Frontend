
import os
import re

products = [
    # Men
    {"img": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=500&q=60", "price": "₹2500", "title": "Classic Checkered Shirt", "desc": "A timeless classic. Perfect for casual outings.", "cat": "Men", "sub_cat": "Shirt"},
    {"img": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&w=500&q=60", "price": "₹4500", "title": "Premium Denim Jacket", "desc": "Rugged and stylish denim jacket.", "cat": "Men", "sub_cat": "Hoodie"}, # Classification catch-all
    {"img": "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?auto=format&fit=crop&w=500&q=60", "price": "₹1800", "title": "Slim Fit Chinos", "desc": "Comfort meets style with these beige chinos.", "cat": "Men", "sub_cat": "Pant"},
    {"img": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?auto=format&fit=crop&w=500&q=60", "price": "₹2200", "title": "Urban Black Hoodie", "desc": "Stay cozy and look cool with this essential black hoodie.", "cat": "Men", "sub_cat": "Hoodie"},
    {"img": "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=500&q=60", "price": "₹1500", "title": "Casual White Shirt", "desc": "Crisp white shirt for a smart casual look.", "cat": "Men", "sub_cat": "Shirt"},
    {"img": "https://images.unsplash.com/photo-1517445312882-56faac29a294?auto=format&fit=crop&w=500&q=60", "price": "₹1200", "title": "Graphic Tee", "desc": "Cool graphic tee for everyday wear.", "cat": "Men", "sub_cat": "Shirt"},
    {"img": "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?auto=format&fit=crop&w=500&q=60", "price": "₹2800", "title": "Black Jeans", "desc": "Essential black jeans with a perfect fit.", "cat": "Men", "sub_cat": "Pant"},
    
    # Women
    {"img": "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?auto=format&fit=crop&w=500&q=60", "price": "₹3200", "title": "Floral Summer Dress", "desc": "Embrace the sun with this beautiful floral dress.", "cat": "Women", "sub_cat": "Dress"},
    {"img": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=500&q=60", "price": "₹2800", "title": "High-Waist Skinny Jeans", "desc": "Flattering high-waist jeans that hug your curves.", "cat": "Women", "sub_cat": "Pant"},
    {"img": "https://images.unsplash.com/photo-1564257631407-4deb1f99d992?auto=format&fit=crop&w=500&q=60", "price": "₹1500", "title": "Elegant White Blouse", "desc": "A versatile white blouse that pairs well with skirts.", "cat": "Women", "sub_cat": "Shirt"},
    {"img": "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?auto=format&fit=crop&w=500&q=60", "price": "₹1900", "title": "Pleated Midi Skirt", "desc": "Flowy pleated skirt in a neutral tone.", "cat": "Women", "sub_cat": "Skirt"},
    {"img": "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?auto=format&fit=crop&w=500&q=60", "price": "₹1200", "title": "Crop Top", "desc": "Trendy crop top for summer vibes.", "cat": "Women", "sub_cat": "Shirt"},
    {"img": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=500&q=60", "price": "₹3500", "title": "Formal Dress", "desc": "Elegant dress for formal occasions.", "cat": "Women", "sub_cat": "Dress"},
    
    # Kids
    # Updated images for Kids
    {"img": "https://images.unsplash.com/photo-1519278409-1f56fdda7e01?auto=format&fit=crop&w=500&q=60", "price": "₹800", "title": "Kids Graphic Tee", "desc": "Playful graphic tee for the little ones.", "cat": "Kids", "sub_cat": "Shirt"},
    {"img": "https://images.unsplash.com/photo-1519457431-44ccd64a579b?auto=format&fit=crop&w=500&q=60", "price": "₹1200", "title": "Kids Denim Overalls", "desc": "Adorable denim overalls for energetic kids.", "cat": "Kids", "sub_cat": "Pant"},
    {"img": "https://images.unsplash.com/photo-1514989940723-e8875ea6ab7d?auto=format&fit=crop&w=500&q=60", "price": "₹1500", "title": "Kids Sport Sneakers", "desc": "Comfortable sneakers designed for active play.", "cat": "Kids", "sub_cat": "Shoes"},
    {"img": "https://images.unsplash.com/photo-1622290291314-e6b9623838ae?auto=format&fit=crop&w=500&q=60", "price": "₹2000", "title": "Girls Party Dress", "desc": "Sparkle and shine with this lovely party dress.", "cat": "Kids", "sub_cat": "Dress"},
    {"img": "https://images.unsplash.com/photo-1503919545889-aef636e10ad4?auto=format&fit=crop&w=500&q=60", "price": "₹900", "title": "Boys Summer Set", "desc": "Comfortable shorts and tee set.", "cat": "Kids", "sub_cat": "Set"}
]

def generate_card(product):
    return f'''
                                    <div class="col-12 col-md-6 col-lg-3">
                                        <div class="card w-100 overflow-hidden" style="border: none; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                                            <img src="{product['img']}"  alt="{product['title']}" style="height: 300px; object-fit: cover;">
                                            <div class="card-body card-body-styling overflow-y-auto">
                                                <h3 class="item-price" style="color: #333; font-weight: bold;">{product['price']}</h3>
                                                <h5 class="card-title">{product['title']}</h5>
                                                <p class="card-text text-muted">{product['desc']}</p>
                                                <a href="#" class="btn btn-dark d-flex justify-content-around align-items-center w-75 mx-auto" style="border-radius: 20px;"> <i class="fa fa-cart-shopping"></i> Add To Cart</a>
                                            </div>
                                        </div>
                                    </div>'''

def update_index():
    with open('index.html', 'r') as f:
        content = f.read()

    # Reuse generating logic, but removed borders
    def create_slides(products_list, items_per_slide):
        slides = []
        for i in range(0, len(products_list), items_per_slide):
            chunk = products_list[i:i+items_per_slide]
            active_class = "active" if i == 0 else ""
            slide_html = f'''                        <div class="carousel-item {active_class}">
                            <div class="container  {'four-item-slide' if items_per_slide==4 else 'two-item-slide' if items_per_slide==2 else 'one-item-slide'}">
                                <div class="row flex-nowrap">
                                    {''.join([generate_card(p) for p in chunk])}
                                </div>
                            </div>
                        </div>'''
            slides.append(slide_html)
        return '\n'.join(slides)

    large_content = create_slides(products, 4)
    med_products = products + products[:4]
    med_content = create_slides(med_products, 2)
    small_products = products[:10]
    small_content = create_slides(small_products, 1)
    
    # Regex replacement for sliders
    # Note: I removed borders <div class="carousel-item active border border-dark"> -> <div class="carousel-item active">
    # And row borders
    
    for section_id, new_html in [("largeScreenSlider", large_content), ("mediumScreenSlider", med_content), ("smallScreenSlider", small_content)]:
        pattern = f'(<section id="{section_id}".*?<div class="carousel-inner">).*?(</div>\\s*?</div>\\s*?<a class="carousel-control-prev")'
        replacement = f'\\1\n{new_html}\n\\2'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open('index.html', 'w') as f:
        f.write(content)
    print("Updated index.html")

def update_all_products(filename='AllProduct.html', filter_cat=None, filter_sub_cat=None):
    if not os.path.exists(filename):
        print(f"File {filename} not found")
        return

    with open(filename, 'r') as f:
        content = f.read()

    relevant_products = products.copy()
    if filter_cat:
        relevant_products = [p for p in relevant_products if p['cat'] == filter_cat]
    if filter_sub_cat:
        # Loose matching for sub_cat (e.g. "Pant" matches "Pant")
        relevant_products = [p for p in relevant_products if filter_sub_cat.lower() in p['sub_cat'].lower()]
        
    if not relevant_products:
        # Fallback if no specific products found to avoid empty page
        print(f"Warning: No products found for {filter_cat}/{filter_sub_cat} in {filename}")
        relevant_products = [p for p in products if p['cat'] == filter_cat] if filter_cat else products

    # Ensure enough items for display
    while len(relevant_products) < 4:
        relevant_products += relevant_products

    rows_html = ""
    for i in range(0, len(relevant_products), 4):
        chunk = relevant_products[i:i+4]
        cards_html = ""
        for p in chunk:
            cards_html += f'''
            <div class="col-12 col-md-6 col-lg-3 mb-4">
                <div class="card overflow-hidden h-100" style="border: none; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                    <img class="card-img-top image-styling" src="{p['img']}" alt="{p['title']}" style="height: 350px; object-fit: cover;">
                    <div class="card-body d-flex flex-column">
                        <h3 style="font-size: 1.5rem; font-weight: bold;">{p['price']}</h3>
                        <h5 class="card-title">{p['title']}</h5>
                        <p class="card-text text-muted small">{p['desc']}</p>
                        <a href="#" class="btn btn-dark mt-auto w-100" style="border-radius: 5px;"> <i class="fa fa-cart-shopping"></i> Add To Cart</a>
                    </div>
                </div>
            </div>'''
        
        rows_html += f'''
        <div class="row justify-content-start align-items-stretch">
            {cards_html}
        </div>'''
        
    pattern = r'(<h2 class="section-title text-center">.*?</h2>)(.*?)(</section>)'
    replacement = f'\\1\n<div class="container mt-5">\n{rows_html}\n</div>\n\\3'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(filename, 'w') as f:
        f.write(new_content)
    print(f"Updated {filename}")

def update_cart():
    if not os.path.exists('cart.html'): return
    with open('cart.html', 'r') as f:
        content = f.read()

    # Better Cart UI
    items_html = ""
    cart_items = [products[3], products[0]]
    
    for p in cart_items:
        items_html += f'''
        <div class="card mb-3 border-0 shadow-sm">
            <div class="card-body">
                <div class="row align-items-center">
                    <div class="col-md-2">
                        <img src="{p['img']}" class="img-fluid rounded" alt="{p['title']}" style="height: 80px; width: 80px; object-fit: cover;">
                    </div>
                    <div class="col-md-4">
                        <h5 class="mb-0">{p['title']}</h5>
                        <small class="text-muted">{p['sub_cat']}</small>
                    </div>
                    <div class="col-md-2">
                         <span class="fw-bold">{p['price']}</span>
                    </div>
                     <div class="col-md-3 d-flex align-items-center">
                        <button class="btn btn-outline-secondary btn-sm rounded-circle" style="width: 30px; height: 30px; padding: 0;">-</button>
                        <input type="text" class="form-control form-control-sm text-center mx-2" value="1" style="width: 40px;">
                        <button class="btn btn-outline-secondary btn-sm rounded-circle" style="width: 30px; height: 30px; padding: 0;">+</button>
                    </div>
                    <div class="col-md-1 text-end">
                        <a href="#!" class="text-danger"><i class="fa fa-trash"></i></a>
                    </div>
                </div>
            </div>
        </div>
        '''

    # Summary Section
    # We replace the whole container content with a better Bootstrap grid
    
    full_cart_html = f'''
    <div class="container my-5">
        <h2 class="mb-4">Shopping Cart</h2>
        <div class="row">
            <div class="col-lg-8">
                {items_html}
            </div>
            <div class="col-lg-4">
                <div class="card border-0 shadow-sm bg-light">
                    <div class="card-body">
                        <h5 class="card-title mb-4">Order Summary</h5>
                        <div class="d-flex justify-content-between mb-2">
                            <span>Subtotal</span>
                            <span>₹4700</span>
                        </div>
                        <div class="d-flex justify-content-between mb-2">
                            <span>Shipping</span>
                            <span>₹0</span>
                        </div>
                        <hr>
                        <div class="d-flex justify-content-between mb-4 fw-bold">
                            <span>Total</span>
                            <span>₹4700</span>
                        </div>
                        <button class="btn btn-dark w-100 py-2">Proceed to Checkout</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    '''
    
    # Replace content between header and footer
    # Use <body> content replacement for simpler handling or specific markers.
    # The original file has <div class="header" id="header"></div> ... <div class="footer" id="footer"></div>
    # Let's target the inner container.
    
    pattern = r'(<div class="header" id="header"></div>)(.*?)(<div class="footer" id="footer"></div>)'
    replacement = f'\\1\n{full_cart_html}\n\\3'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open('cart.html', 'w') as f:
        f.write(content)
    print("Updated cart.html")

def update_contact():
    if not os.path.exists('contact.html'): return
    with open('contact.html', 'r') as f:
        content = f.read()
        
    form_html = f'''
    <div class="container my-5">
        <div class="row align-items-center shadow-lg rounded overflow-hidden">
            <div class="col-md-6 p-0">
                <img src="https://images.unsplash.com/photo-1596524430615-b46476dd9f56?auto=format&fit=crop&w=800&q=80" alt="Contact Us" class="img-fluid w-100 h-100" style="object-fit: cover; min-height: 500px;">
            </div>
            <div class="col-md-6 p-5 bg-white">
                <h2 class="mb-4 text-center fw-bold">Get In Touch</h2>
                <form>
                    <div class="mb-3">
                        <label for="name" class="form-label">Full Name</label>
                        <input type="text" class="form-control" id="name" placeholder="John Doe">
                    </div>
                    <div class="mb-3">
                        <label for="email" class="form-label">Email Address</label>
                        <input type="email" class="form-control" id="email" placeholder="name@example.com">
                    </div>
                    <div class="mb-4">
                        <label for="message" class="form-label">Message</label>
                        <textarea class="form-control" id="message" rows="4" placeholder="How can we help?"></textarea>
                    </div>
                    <button type="button" class="btn btn-dark w-100 py-2">Send Message</button>
                </form>
            </div>
        </div>
    </div>
    '''
    
    # Replace content between header and footer
    pattern = r'(<div class="header" id="header"></div>)(.*?)(<div class="footer" id="footer"></div>)'
    replacement = f'\\1\n{form_html}\n\\3'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open('contact.html', 'w') as f:
        f.write(content)
    print("Updated contact.html")

def update_login():
    if not os.path.exists('login.html'): return
    with open('login.html', 'r') as f:
        content = f.read()
        
    login_html = '''
    <div class="container d-flex justify-content-center align-items-center" style="min-height: 80vh;">
        <div class="card border-0 shadow-lg p-4" style="width: 100%; max-width: 400px; border-radius: 15px;">
            <div class="card-body">
                <h3 class="text-center mb-4 fw-bold">Welcome Back</h3>
                <form>
                    <div class="mb-3">
                        <label for="email" class="form-label">Email address</label>
                        <input type="email" class="form-control" id="email" placeholder="name@example.com">
                    </div>
                    <div class="mb-4">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" class="form-control" id="password" placeholder="••••••••">
                    </div>
                    <button type="button" class="btn btn-dark w-100 py-2 mb-3" onclick="checker()">Login</button>
                     <p class="text-center small text-muted">Don't have an account? <a href="#" class="text-decoration-none">Sign up</a></p>
                </form>
            </div>
        </div>
    </div>
    '''
    
    pattern = r'(<div class="header" id="header"></div>)(.*?)(<div class="footer" id="footer"></div>)'
    replacement = f'\\1\n{login_html}\n\\3'
    
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open('login.html', 'w') as f:
        f.write(content)
    print("Updated login.html")

if __name__ == "__main__":
    update_index()
    update_all_products("AllProduct.html", None)
    
    # Categories and Filtering
    update_all_products("MenAll.html", "Men")
    update_all_products("MenShirts.html", "Men", "Shirt")
    update_all_products("MenPants.html", "Men", "Pant")
    update_all_products("MenHoodies.html", "Men", "Hoodie")
    
    update_all_products("WomenAll.html", "Women")
    update_all_products("WomenDresses.html", "Women", "Dress")
    update_all_products("WomenPants.html", "Women", "Pant")
    update_all_products("WomenSkirts.html", "Women", "Skirt")
    
    update_all_products("kids.html", "Kids")
    
    update_cart()
    update_contact()
    update_login()
