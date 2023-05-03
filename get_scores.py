import glob
from nltk.sentiment import SentimentIntensityAnalyzer


def get_scores():
    filepaths = glob.glob("diary/*txt")

    # Create a couple of empty lists
    pos_values = []
    neg_values = []

    analyzer = SentimentIntensityAnalyzer()

    # Loop for all txt records
    for filepath in filepaths:
        with open(filepath) as file:
            content = file.read()

        # Analyse text and generate scores
        result = analyzer.polarity_scores(content)

        # Append the scores to the lists
        pos_values.append(result["pos"])
        neg_values.append(result["neg"])

    # Take date from the filepath
    dates = [name.strip(".txt").strip("diary/") for name in filepaths]
    return pos_values, neg_values, dates


if __name__ == "__main__":
    pos, neg = get_scores()
    print(pos)
    print(neg)
