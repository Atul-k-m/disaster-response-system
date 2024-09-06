from flask import Flask, jsonify
from data_collection.api_fetcher import fetch_x_data, fetch_news_data
from nlp_processing.text_analysis import extract_named_entities, sentiment_analysis
from nlp_processing.classification import classify_disaster
from app.models import store_data  

def create_app():
  """Creates a Flask application instance with routes and error handling."""
  app = Flask(__name__)

  @app.route('/fetch-data', methods=['GET'])
  def fetch_data():
    """
    Fetches disaster data, processes it, stores it, and returns a success message.

    Handles potential errors from data fetching and storage.
    """
    query = "earthquake OR flood OR wildfire OR funny"
    try:
      x_data = fetch_x_data(query)
      news_data = fetch_news_data(query)
    except Exception as e:
     
      return jsonify({"error": f"Error fetching data: {str(e)}"}), 500

    # Process and store the data
    processed_data = []
    for item in x_data.get('data', []):
      entities = extract_named_entities(item['text'])
      sentiment = sentiment_analysis(item['text'])
      category = classify_disaster(item['text'])
      processed_data.append({
          'text': item['text'],
          'entities': entities,
          'sentiment': sentiment,
          'category': category
      })

    try:
      store_data('disasters', processed_data)
    except Exception as e:
      #STORAGE HANDLING
      return jsonify({"error": f"Error storing data: {str(e)}"}), 500

    return jsonify({"message": "Data fetched and processed successfully"})

  @app.errorhandler(Exception)  # Handle all uncaught exceptions
  def handle_exception(error):
    """Handles any uncaught exceptions and returns a generic error message."""
    return jsonify({"error": f"An internal error occurred: {str(error)}"}), 500

  return app


app = create_app()

if __name__ == '__main__':
  app.run(debug=True)