import pandas as pd
import random

def generate_movie_reviews(num_reviews, genre, sentiment):
    positive_templates = [
        f"This {genre} movie is {random.choice(['absolutely fantastic', 'truly remarkable', 'incredibly engaging'])}! The {genre.lower()} scenes are {random.choice(['intense', 'exciting', 'riveting'])}, and the plot is {random.choice(['engaging', 'captivating', 'compelling'])}. I highly recommend it.",
        f"I'm amazed by this {genre} movie! The {genre.lower()} scenes are {random.choice(['mind-blowing', 'spectacular', 'extraordinary'])}, and the storyline is {random.choice(['remarkable', 'outstanding', 'superb'])}. A must-watch!",
        f"This {genre} film is a gem. The {genre.lower()} scenes are {random.choice(['captivating', 'spellbinding', 'mesmerizing'])}, and the plot is {random.choice(['riveting', 'absorbing', 'intriguing'])}. I couldn't look away.",
        f"I couldn't be happier with this {genre} movie. The {genre.lower()} scenes are {random.choice(['phenomenal', 'awe-inspiring', 'breathtaking'])}, and the storyline is {random.choice(['exceptional', 'brilliant', 'masterful'])}. Truly a cinematic delight.",
        f"A cinematic triumph! This {genre} movie exceeded all my expectations. The {genre.lower()} scenes are {random.choice(['jaw-dropping', 'awe-inspiring', 'stunning'])}, and the plot is {random.choice(['exceptional', 'extraordinary', 'fantastic'])}. A must-see masterpiece.",

    ]

    negative_templates = [
        f"I found this {genre} movie {random.choice(['disappointing', 'underwhelming', 'lacking'])}. The {genre.lower()} scenes lacked {random.choice(['depth', 'impact', 'suspense'])}, and the characters were not well-developed. Overall, it was a letdown.",
        f"This {genre} movie didn't meet my expectations. The {genre.lower()} scenes were {random.choice(['subpar', 'dull', 'uninspiring'])}, and the storyline was {random.choice(['predictable', 'uninteresting', 'disjointed'])}. I wouldn't recommend it.",
        f"This {genre} film fell short for me. The {genre.lower()} scenes lacked {random.choice(['intensity', 'intrigue', 'drama'])}, and the plot felt {random.choice(['predictable', 'formulaic', 'stale'])}. A disappointing experience.",
        f"Unfortunately, this {genre} movie didn't impress me. The {genre.lower()} scenes were {random.choice(['mediocre', 'ordinary', 'unremarkable'])}, and the storyline was {random.choice(['lackluster', 'uninspiring', 'forgettable'])}. Not worth the hype.",
        f"A cinematic letdown. This {genre} movie failed to deliver. The {genre.lower()} scenes were {random.choice(['disappointing', 'lackluster', 'forgettable'])}, and the plot was {random.choice(['weak', 'unconvincing', 'uninspired'])}. Save your time.",

    ]

    neutral_templates = [
        f"The {genre} movie had an average plot. It neither impressed nor disappointed me. The {genre.lower()} scenes were okay.",
        f"This {genre} movie provided a middle-of-the-road experience. The {genre.lower()} scenes were neither outstanding nor terrible. It's an average watch.",
        f"This {genre} film is a mixed bag. While the {genre.lower()} scenes had moments of {random.choice(['brilliance', 'excitement', 'emotion'])}, the overall plot left me feeling {random.choice(['indifferent', 'neutral', 'undecided'])}.",
        f"A balanced {genre} movie. The {genre.lower()} scenes were neither exceptional nor subpar. The storyline was {random.choice(['moderate', 'adequate', 'acceptable'])}.",
        f"This {genre} movie falls in the middle for me. The {genre.lower()} scenes were {random.choice(['average', 'decent', 'fair'])}, and the plot was {random.choice(['middling', 'ordinary', 'standard'])}. It's neither great nor terrible.",

    ]

    very_positive_templates = [
        f"This {genre} movie is a masterpiece! The {genre.lower()} scenes are {random.choice(['jaw-dropping', 'awe-inspiring', 'magical'])}, and the storyline is {random.choice(['phenomenal', 'extraordinary', 'captivating'])}. A must-see!",
        f"I'm absolutely blown away by this {genre} movie! The {genre.lower()} scenes are {random.choice(['stunning', 'breathtaking', 'exquisite'])}, and the plot is {random.choice(['exceptional', 'outstanding', 'superb'])}. Highly recommended.",
        f"A cinematic marvel! This {genre} movie is a triumph. The {genre.lower()} scenes are {random.choice(['mesmerizing', 'spellbinding', 'enchanting'])}, and the plot is {random.choice(['compelling', 'masterful', 'brilliant'])}. An absolute gem.",
        f"This {genre} movie is pure gold. The {genre.lower()} scenes are {random.choice(['mesmerizing', 'captivating', 'spellbinding'])}, and the storyline is {random.choice(['masterful', 'incredible', 'unforgettable'])}. A work of art.",
        f"I'm in awe of this {genre} movie! The {genre.lower()} scenes are {random.choice(['extraordinary', 'mind-blowing', 'awe-inspiring'])}, and the plot is {random.choice(['remarkable', 'outstanding', 'exceptional'])}. Truly a cinematic treasure.",

    ]

    very_negative_templates = [
        f"This {genre} movie is a disaster. The {genre.lower()} scenes are {random.choice(['terrible', 'awful', 'abysmal'])}, and the storyline is {random.choice(['atrocious', 'horrendous', 'dreadful'])}. Avoid at all costs.",
        f"I strongly discourage watching this {genre} movie. The {genre.lower()} scenes are {random.choice(['disastrous', 'appalling', 'revolting'])}, and the plot is {random.choice(['miserable', 'ludicrous', 'absurd'])}. Terrible experience.",
        f"A cinematic catastrophe! This {genre} movie is an utter failure. The {genre.lower()} scenes are {random.choice(['disappointing', 'horrible', 'disastrous'])}, and the storyline is {random.choice(['unbearable', 'ludicrous', 'atrocious'])}. Save yourself the agony.",
        f"This {genre} movie is a train wreck. The {genre.lower()} scenes are {random.choice(['disastrous', 'abominable', 'wretched'])}, and the plot is {random.choice(['atrocious', 'pitiful', 'tragic'])}. I can't believe I wasted my time on this.",
        f"Stay far away from this {genre} movie. The {genre.lower()} scenes are {random.choice(['dreadful', 'horrendous', 'appalling'])}, and the storyline is {random.choice(['atrocious', 'disastrous', 'unwatchable'])}. One of the worst movies I've ever seen.",

    ]

    templates_by_sentiment = {
        "positive": positive_templates,
        "negative": negative_templates,
        "neutral": neutral_templates,
        "very positive": very_positive_templates,
        "very negative": very_negative_templates,
    }

    reviews = []
    for _ in range(num_reviews):
        template = random.choice(templates_by_sentiment[sentiment])
        review = template.replace("{genre}", genre)
        reviews.append(review)

    return reviews

genres = ["Action", "Drama", "Comedy", "Sci-Fi", "Thriller", "Romance", "Horror", "Adventure", "Fantasy", "Mystery", "Animation", "Biography", "History", "Documentary", "Music", "Sport", "War", "Western", "Musical", "Family", "Superhero", "Crime", "Suspense", "Supernatural", "Historical Fiction"]
sentiments = ["positive", "negative", "neutral", "very positive", "very negative"]

reviews = []
labels = []

for genre in genres:
    for sentiment in sentiments:
        genre_reviews = generate_movie_reviews(10, genre, sentiment)
        reviews.extend(genre_reviews)
        labels.extend([f"{genre} ({sentiment})"] * 10)

data = list(zip(reviews, labels))
random.shuffle(data)

df = pd.DataFrame(data, columns=["text", "genre"])

df.to_csv("movie_reviews_dataset_large_v7.csv", index=False)