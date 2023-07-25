from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

blog_posts = [
    {
        'title': 'The AI Revolutions',
        'content': '''Artificial Intelligence (AI) has been making waves in various industries, revolutionizing the way we live and work. In 2023, we have witnessed remarkable advancements and breakthroughs in the AI landscape.

        AI-powered technologies are shaping our daily lives, from voice assistants like Siri and Alexa to autonomous vehicles. But it's not just limited to consumer applications. Industries such as healthcare, finance, and manufacturing have also embraced AI to optimize processes and drive innovation.

        In healthcare, AI has enabled faster and more accurate diagnostics, assisting doctors in detecting diseases and recommending treatment plans. It has also played a crucial role in drug discovery and development, significantly reducing the time and cost involved.

        The finance industry has leveraged AI algorithms for fraud detection, risk assessment, and algorithmic trading. AI-powered chatbots have enhanced customer service by providing personalized support and assistance.

        Furthermore, AI is transforming manufacturing by enabling predictive maintenance, optimizing supply chain management, and improving product quality through computer vision systems.

        The rapid pace of AI advancements raises important ethical considerations. Ensuring transparency, fairness, and accountability in AI decision-making processes is crucial. AI should be designed and implemented with proper regulations and guidelines to avoid unintended consequences.

        As we look towards the future, AI will continue to drive innovation and shape our society. It presents both immense opportunities and challenges that require collaborative efforts from researchers, policymakers, and industry leaders.

        Let's embrace the AI revolutions and harness its potential to create a better and more sustainable future.''',
        'author': 'John Doe',
        'date': '2023-07-19'
    },
    {
        'title': 'The Modern Era',
        'content': '''Artificial Intelligence (AI) has been making waves in various industries, revolutionizing the way we live and work. In 2023, we have witnessed remarkable advancements and breakthroughs in the AI landscape.

        ... (content of the second blog post) ...

        Let's embrace the AI revolutions and harness its potential to create a better and more sustainable future.''',
        'author': 'John Doe',
        'date': '2023-07-19'
    }
]


# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=blog_posts)

@app.route('/blog/<int:post_id>')
def post(post_id):
    post = blog_posts[post_id]
    return render_template('post.html', post=post)

@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        current_date = date.today().strftime("%Y-%m-%d") 

        new_post = {
            'title': title,
            'content': content,
            'author': author,
            'date': current_date
        }

        blog_posts.append(new_post)

        return render_template('write.html', success=True)

    return render_template('write.html', success=False, current_date=date.today().strftime("%Y-%m-%d"))

if __name__ == '__main__':
    app.run(debug=True)












