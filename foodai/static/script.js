function createHTML() {
    // Create the header
    const header = document.createElement('header');
header.innerHTML = `
    <div class="container">
        <img src="logo.png" alt="FoodAI Logo" class="logo">
        <h1><a href="#hero">FoodAI</a></h1>
        <p>Nutrition Meets Technology for Your Fitness Success</p>
        <nav>
            <ul>
                <li><a href="#products">Products</a></li>
                <li><a href="#ai-helper">AI Helper</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
        <div class="login-container">
            <a href="login.html" class="btn">Login</a>
        </div>
    </div>
`;

    document.body.appendChild(header);

    // Create the hero section
    const heroSection = document.createElement('section');
    heroSection.id = "hero";
    heroSection.innerHTML = `
        <div class="container">
            <h2>Fuel Your Fitness with FoodAI</h2>
            <p>Choose from our wide range of protein, meals, and drinks designed to support your fitness goals. Let our AI guide you to the perfect choice.</p>
            <a href="#products" class="btn">Explore Products</a>
        </div>
    `;
    document.body.appendChild(heroSection);

    // Create the products section
    const productsSection = document.createElement('section');
    productsSection.id = "products";
    productsSection.className = "container";
    productsSection.innerHTML = `
        <h2>Our Products</h2>
        <div class="product-list">
            <div class="product">
                <a href="protein.html" class="product-link">
                    <img src="https://m.media-amazon.com/images/I/81rkH4m7O3L._AC_UF1000,1000_QL80_.jpg" alt="Produit Amazon" width="600" height="300">
                    <h3>Protein Powders</h3>
                    <p>Boost your muscle recovery with our high-quality protein powders.</p>
                </a>
            </div>
            <div class="product">
                <a href="healthy-meals.html" class="product-link">
                    <img src="https://www.verywellfit.com/thmb/DmfPZY2OPUSn3TfhCq8uB0Lw9y0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/VWFit-Meal-Plan-Journey-1-Week-Healthy-and-Balance-Meal-Plan-6ee43578918947a4b687922d614f2be3.jpg" alt="Plan de Repas Sain" width="600" height="300">
                    <h3>Healthy Meals</h3>
                    <p>Delicious, balanced meals to keep your energy levels high.</p>
                </a>
            </div>
            <div class="product">
                <a href="energy-drinks.html" class="product-link">
                    <img src="https://maxesport.gg/medias/2024/09/Brand-Banner_Rez.webp" alt="Bannière de Marque" width="600" height="300">
                    <h3>Energy Drinks</h3>
                    <p>Stay hydrated and energized with our refreshing energy drinks.</p>
                </a>
            </div>
        </div>
    `;
    document.body.appendChild(productsSection);

    // Create the AI helper section
    const aiHelperSection = document.createElement('section');
    aiHelperSection.id = "ai-helper";
    aiHelperSection.className = "container";
    aiHelperSection.innerHTML = `
        <h2>AI-Powered Nutrition Guide</h2>
        <p>Let our AI help you find the perfect products based on your fitness goals. Whether you want to gain muscle, lose weight, or maintain a balanced diet, our AI will recommend the best options for you.</p>
        <a href="AIHelper.html" class="btn">Try the AI Helper</a>
    `;
    document.body.appendChild(aiHelperSection);

    // Create the about section
    const aboutSection = document.createElement('section');
    aboutSection.id = "about";
    aboutSection.className = "container";
    aboutSection.innerHTML = `
        <h2>About FoodAI</h2>
        <p>
            At FoodAI, we believe that fitness is a journey, and the right nutrition is key to success. Our mission is to provide high-quality food products at the gym that are tailored to your personal fitness goals.<br>
            With the help of AI, we take the guesswork out of nutrition and guide you to make the best choices for your body.
        </p>
    `;
    document.body.appendChild(aboutSection);

    // Create the footer section
    const footer = document.createElement('footer');
    footer.id = "contact";
    footer.className = "container";
    footer.innerHTML = `
        <h2>Contact Us</h2>
        <p>Have questions or need help? Reach out to us:</p>
        <ul>
            <li>Email: support@foodai.com</li>
            <li>Phone: (+33) 0661516641</li>
        </ul>
    `;
    document.body.appendChild(footer);
}

// Call the function to create HTML when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', createHTML);
