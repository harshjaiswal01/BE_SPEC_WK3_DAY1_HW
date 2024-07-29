from flask import Flask, request, jsonify

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def sort_videos(video_titles):
    return sorted(video_titles)

@app.route('/search', methods=['GET'])
def search_video():
    query = request.args.get('title')
    if not query:
        return jsonify({"error": "No search query provided"}), 400
    
    sorted_videos = sort_videos(video_titles)
    index = binary_search(sorted_videos, query)
    
    if index != -1:
        return jsonify({"message": f"Video '{query}' found at index {index}.", "video": sorted_videos[index]})
    else:
        return jsonify({"message": f"Video '{query}' not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
