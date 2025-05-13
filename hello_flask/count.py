from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

# Redis connection
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/count')
def count():
    visitor_count = redis_client.incr('counter')  
    return render_template('count.html', count=visitor_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
