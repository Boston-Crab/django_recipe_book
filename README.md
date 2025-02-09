# DJANGO RECIPE BOOK
Django backend project using <a href="https://www.themealdb.com/api.php" target="_blank">The Meal DB recipe api</a>

Website preview link: **The website is no longer hosted.**

### --- Features ---
<ul>
  <li>Recipes retrieval from API</li>
  <li>Sign-up, Login, Logout</li>
  <li>Change email/password</li>
  <li>Like/Dislike a recipe</li>
  <li>User written a comments for every recipe</li>
</ul>

### --- Known Issues ---
<ul>
  <li>Frontend is not displayed correctly on phones/small screens</li>
</ul>

### --- Instructions To Run With LocalHost ---
1. Create and activate a virtual environment:
  - `python -m venv venv`
  - `For Linux: source venv/bin/activate or for Windows: .\venv\Scripts\activate`
2. Install requirements:
  - `pip install -r requirements.txt`
3. Change DEBUG and DEVELOPMENT_MODE in recipe_book/settings.py to:
  - `DEBUG = os.getenv("DEBUG", "True") == "True"`
  - `DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "True") == "True"`
