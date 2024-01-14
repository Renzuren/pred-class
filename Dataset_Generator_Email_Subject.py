import pandas as pd
import random

def generate_email_subjects(num_subjects, categories, keywords):
    subjects = []
    labels = []

    for _ in range(num_subjects):
        category = random.choice(categories)
        keyword = random.choice(keywords[category])

        template = f"{keyword} {random.choice(['update', 'announcement', 'news', 'opportunity'])}"
        subject = template.capitalize()

        subjects.append(subject)
        labels.append(category)

    return subjects, labels

categories = ["Technology", "Health", "Finance", "Travel", "Food",
              "Fashion", "Sports", "Education", "Entertainment", "Science",
              "Art", "Business", "Music", "Fitness", "Home",
              "Gaming", "Environment", "Books", "Pets", "Movies",
              "Automotive", "Social Media", "Career", "Shopping", "Weather"]  # 25 categories

keywords = {
    "Technology": ["Innovation", "Gadgets", "Smartphones", "Artificial Intelligence", "Programming",
                   "Data Science", "Cloud Computing", "Cybersecurity", "Augmented Reality", "Virtual Reality",
                   "Blockchain", "Machine Learning", "Internet of Things", "Robotics", "Tech Startups",
                   "Mobile Apps", "Web Development", "Computer Vision", "Big Data", "Quantum Computing",
                   "IT Infrastructure", "Software Engineering", "Network Security", "Open Source",
                   "Digital Transformation"],

    "Health": ["Wellness", "Fitness", "Nutrition", "Medical", "Mental Health",
               "Dietary Supplements", "Healthy Recipes", "Well-being", "Weight Loss", "Exercise",
               "Alternative Medicine", "Healthcare Trends", "Medical Research", "Preventive Care", "Holistic Health",
               "Physical Therapy", "Healthy Lifestyle", "Mindfulness", "Yoga", "Counseling",
               "Vitamins", "Healthy Aging", "Self-care", "Health Technology", "Medical Innovations"],

    "Finance": ["Investment", "Budgeting", "Stock Market", "Financial Planning", "Cryptocurrency",
                "Personal Finance", "Retirement Planning", "Wealth Management", "Economic Trends", "Real Estate",
                "Credit Management", "Savings Tips", "Financial Education", "Insurance", "Tax Planning",
                "Fintech", "Global Markets", "Entrepreneurial Finance", "Financial Literacy", "Asset Allocation",
                "Market Analysis", "Blockchain in Finance", "Peer-to-peer Lending", "Credit Cards", "Robo-Advisors"],

    "Travel": ["Destinations", "Vacation Deals", "Adventure", "Travel Tips", "Hotels",
               "Cruises", "Budget Travel", "Solo Travel", "Family Vacations", "Luxury Travel",
               "Cultural Experiences", "Beach Resorts", "Mountain Retreats", "City Breaks", "Historical Sites",
               "Travel Gadgets", "Airfare Discounts", "Travel Safety", "Food Tourism", "Travel Apps",
               "Ecotourism", "Road Trips", "Backpacking", "Travel Insurance", "Digital Nomad Lifestyle"],

    "Food": ["Recipes", "Cuisine", "Cooking Tips", "Food Trends", "Restaurant Reviews",
             "Healthy Eating", "Vegetarian & Vegan", "International Flavors", "Desserts", "Beverages",
             "Gourmet Cooking", "Quick Meals", "Food Photography", "Kitchen Gadgets", "Meal Prep",
             "Farm-to-Table", "Local Ingredients", "Street Food", "BBQ & Grilling", "Cookbook Recommendations",
             "Food Festivals", "Wine & Spirits", "Coffee Culture", "Dining Etiquette", "Food History"],

    "Fashion": ["Style Tips", "Trends", "Fashion Shows", "Shopping Deals", "Accessories",
                "Designer Spotlights", "Street Fashion", "Sustainable Fashion", "Vintage Finds", "Seasonal Fashion",
                "Beauty Tips", "Makeup Trends", "Hairstyle Ideas", "Fashion Influencers", "Fashion Photography",
                "Celebrity Fashion", "DIY Fashion", "Luxury Brands", "Fashion Events", "Fashion History",
                "Online Shopping", "Thrift Store Finds", "Fashion for All Body Types", "Fashion and Technology",
                "Workplace Fashion"],

    "Sports": ["Games", "Scores", "Athlete Interviews", "Training Tips", "Sports Events",
               "Team Sports", "Extreme Sports", "Fitness Challenges", "Sports Gear", "Fan Experience",
               "Olympic Games", "Athletics", "Sports Medicine", "Outdoor Adventures", "Sports Psychology",
               "E-sports", "Youth Sports", "Sports Nutrition", "Sports Betting", "Behind the Scenes",
               "Athlete Profiles", "Sports Science", "Motorsports", "Sports Business", "Inspirational Sports Stories"],

    "Education": ["Learning Resources", "Study Tips", "Online Courses", "Education Technology", "Student Life",
                  "STEM Education", "Language Learning", "Study Abroad", "Career Development", "Educational Apps",
                  "E-learning Platforms", "Teaching Strategies", "College Life", "Literacy Programs",
                  "Learning Disabilities",
                  "Educational Events", "Teacher Spotlights", "Parental Involvement", "MOOCs", "Educational Podcasts",
                  "Edutainment", "Virtual Classrooms", "Education Policy", "Educational Psychology", "Art Education"],

    "Entertainment": ["Celebrity News", "Movie Reviews", "TV Shows", "Concerts", "Events",
                      "Award Shows", "Red Carpet Fashion", "Celebrity Interviews", "Film Festivals",
                      "Entertainment Industry",
                      "Behind the Scenes", "Film Criticism", "Documentaries", "Musical Performances", "Cultural Events",
                      "Upcoming Releases", "Pop Culture", "Fan Theories", "Reality TV", "Streaming Services",
                      "Gaming Culture", "Comedy Shows", "Theater Productions", "Entertainment Technology", "Fan Clubs"],

    "Science": ["Discoveries", "Research", "Space Exploration", "Innovation", "Environmental Science",
                "Biotechnology", "Scientific Breakthroughs", "Astronomy", "Physics", "Chemistry",
                "Biology", "Geology", "Climate Science", "Medical Research", "Scientific Ethics",
                "Robotics", "Oceanography", "Neuroscience", "Genetics", "Paleontology",
                "Scientific Experiments", "Science Communication", "Science History", "Women in Science",
                "Data Science"],

    "Art": ["Gallery Exhibitions", "Artists Spotlight", "Art Critiques", "Art Auctions", "Creative Inspiration",
            "Contemporary Art", "Classical Art", "Street Art", "Digital Art", "Sculpture",
            "Art Installations", "Art and Technology", "Art Restoration", "Art Movements", "Art History",
            "Art Collecting", "Public Art", "Performance Art", "Mixed Media", "Cultural Heritage",
            "Art Education", "Art Therapy", "Art Fairs", "Art and Society", "Artistic Expression"],

    "Business": ["Entrepreneurship", "Startups", "Business Trends", "Leadership", "Corporate News",
                 "Business Strategy", "Innovation in Business", "Marketing Strategies", "Finance in Business",
                 "Social Responsibility",
                 "Small Business Tips", "Global Business", "E-commerce", "Supply Chain Management",
                 "Customer Experience",
                 "Business Technology", "Entrepreneurial Mindset", "Workplace Culture", "Business Ethics",
                 "Success Stories",
                 "Business Networking", "Corporate Social Media", "Investor Relations", "Business Analysis",
                 "Future of Work"],

    "Music": ["New Releases", "Concerts", "Music Festivals", "Artist Interviews", "Music Genres",
              "Music Reviews", "Album Recommendations", "Music History", "Local Music Scene", "Classical Music",
              "Indie Music", "Music Production", "Songwriting", "Music Education", "Musical Instruments",
              "Live Performances", "Music Technology", "Music and Culture", "Music and Mental Health", "Music Business",
              "Music Discoveries", "Soundtracks", "Favorite Playlists", "Music Festivals", "International Music"],

    "Fitness": ["Workouts", "Training Programs", "Nutrition Tips", "Fitness Challenges", "Healthy Living",
                "Yoga", "Cardio Workouts", "Strength Training", "Mental Fitness", "Outdoor Fitness",
                "Fitness Gear", "Athlete Spotlights", "Fitness Trends", "Group Fitness", "Crossfit",
                "Mind-body Exercises", "Recovery Techniques", "Fitness Technology", "Wellness Retreats",
                "Holistic Fitness",
                "Healthy Recipes", "Fitness Competitions", "Fitness for Beginners", "Senior Fitness", "Fitness Apps"],

    "Home": ["Interior Design", "Home Improvement", "Organizing Tips", "DIY Projects", "Decor Ideas",
             "Home Maintenance", "Smart Home Technology", "Gardening", "Sustainable Living", "Pet-friendly Homes",
             "Home Office Ideas", "House Tours", "Home Decor Trends", "Home Renovations", "Furniture Design",
             "Kitchen Design", "Bathroom Ideas", "Bedroom Makeovers", "Outdoor Living", "Home Energy Efficiency",
             "Home Security", "Real Estate Tips", "Apartment Living", "Home Buying Guide", "Home Entertainment"],

    "Gaming": ["Video Game News", "Game Reviews", "Gaming Events", "Tips and Cheats", "Gaming Hardware",
               "Esports", "Gaming Communities", "Game Development", "Virtual Reality Games", "Mobile Gaming",
               "PC Gaming", "Console Gaming", "Gaming Industry", "Game Design", "Gaming Culture",
               "Streaming Games", "Retro Gaming", "Indie Games", "Gaming Technology", "Gaming Tournaments",
               "Game Collecting", "Gaming Conventions", "Online Multiplayer Games", "Gaming Accessories",
               "Gaming Merchandise"],

    "Environment": ["Climate Change", "Conservation", "Green Living", "Environmental Activism",
                    "Eco-friendly Practices",
                    "Sustainable Development", "Renewable Energy", "Waste Reduction", "Biodiversity",
                    "Wildlife Conservation",
                    "Ocean Conservation", "Air Quality", "Environmental Education", "Zero Waste Lifestyle",
                    "Carbon Footprint",
                    "Eco-friendly Technology", "Green Architecture", "Permaculture", "Environmental Justice",
                    "Sustainable Fashion",
                    "Environmental Policies", "Eco-tourism", "Water Conservation", "Green Products",
                    "Circular Economy"],

    "Books": ["Book Recommendations", "Author Interviews", "Book Reviews", "Literary Events", "Reading Lists",
              "Classic Literature", "Contemporary Fiction", "Mystery and Thrillers", "Science Fiction", "Fantasy",
              "Non-fiction", "Biographies", "Book Club Discussions", "Children's Books", "Young Adult Fiction",
              "Science Fiction", "Fantasy", "Biography/Memoir", "Young Adult", "Historical Fiction", "Poetry", "Book Adaptations", "Book Festivals", "Writing Tips", "Bookstores",
    "Publishing Industry", "Literary Awards", "Book Trends", "Reading Habits", "Book News"],

    "Pets": ["Pet Care Tips", "Pet Adoption", "Animal Welfare", "Pet Health", "Cute Pet Stories",
             "Pet Training", "Pet Products", "Pet Grooming", "Pet Behavior", "Pet Insurance",
             "Exotic Pets", "Pet-friendly Travel", "Wildlife", "Animal Companionship", "Pet Photography",
             "Famous Pets", "Adorable Videos", "Pet-Friendly Events", "Pet Charity", "Pet Fashion",
             "Aquariums", "Zoos", "Bird Watching", "Reptiles", "Small Pets"],

    "Movies": ["Film Reviews", "Movie Trailers", "Actor Interviews", "Film Festivals", "Cinematic Trends",
               "Classic Films", "Blockbusters", "Indie Films", "Documentaries", "Animated Movies",
               "Cinematography", "Film Genres", "Movie Soundtracks", "Film Criticism", "Behind the Scenes",
               "Upcoming Releases", "Movie Theaters", "Streaming Platforms", "Film History", "Oscar Contenders",
               "Cult Classics", "Directors' Spotlight", "Film Industry News", "Movie Merchandise", "Movie Awards"],

    "Automotive": ["Car Reviews", "Auto Shows", "Driving Tips", "Automotive Technology", "Motorcycles",
                   "Electric Vehicles", "Concept Cars", "Luxury Cars", "Classic Cars", "Auto Racing",
                   "SUVs", "Trucks", "Car Maintenance", "Road Safety", "Car Accessories",
                   "Hybrid Cars", "Fuel Efficiency", "Automotive Design", "Innovations in Vehicles", "Car Rentals",
                   "Vintage Cars", "Driverless Cars", "Traffic Updates", "Motor Shows", "Automotive Events"],

    "Social Media": ["Social Trends", "Platform Updates", "Influencer News", "Social Media Marketing", "Digital Culture",
                     "Content Creation", "Social Media Strategy", "Online Communities", "Social Impact", "Social Media and Business",
                     "Viral Content", "Digital Influencers", "User-generated Content", "Social Media Analytics", "Online Presence",
                     "Digital Marketing", "Tech and Social Media", "Privacy on Social Media", "Social Media for Small Businesses", "Social Media Campaigns",
                     "Social Media Psychology", "Social Media and Mental Health", "Emerging Platforms", "Social Media Trends", "Social Media Policies"],

    "Career": ["Job Opportunities", "Career Advice", "Professional Development", "Networking Tips", "Workplace Trends",
               "Remote Work", "Freelancing", "Job Interviews", "Resume Building", "Entrepreneurship",
               "Leadership", "Work-Life Balance", "Corporate Culture", "Career Transitions", "Success Stories",
               "Skill Development", "Job Search Strategies", "Career Fairs", "Salary Negotiation", "Workplace Productivity",
               "Diversity in the Workplace", "Employee Well-being", "Job Satisfaction", "Women in the Workplace", "Job Security"],

    "Shopping": ["Sales and Discounts", "Shopping Guides", "Fashion Deals", "Consumer Reviews", "Online Shopping",
                 "Retail Trends", "E-commerce", "Luxury Shopping", "Thrift Shopping", "Shopping for a Cause",
                 "Personal Styling", "Seasonal Sales", "Product Recommendations", "Gift Ideas", "Shopping Apps",
                 "Consumer Electronics", "Home Goods", "Beauty Products", "Gourmet Food", "Fashion Accessories",
                 "Shopping Hauls", "Sustainable Shopping", "Shopping on a Budget", "Shopping Destinations", "Shopping Events"],

    "Weather": ["Local Forecasts", "Seasonal Updates", "Weather Events", "Travel Advisories", "Climate Reports",
                "Natural Disasters", "Meteorology", "Climate Change", "Weather Phenomena", "Extreme Weather",
                "Weather Technology", "Weather Preparedness", "Weather and Health", "Global Weather Patterns", "Weather Photography",
                "Historical Weather Events", "Weather Apps", "Climate Action", "Weather and Agriculture", "Weather News",
                "Space Weather", "Weather Forecasting", "Weather and Tourism", "Weather Research", "Weather Monitoring"]
}


num_subjects = 250000 # gawin ko na 250k

subjects, labels = generate_email_subjects(num_subjects, categories, keywords)

df = pd.DataFrame({"Subject": subjects, "Category": labels})

print(df)
df.to_csv("email_subjects_dataset_large.csv", index=False)