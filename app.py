from flask import Flask, request, jsonify
import plotly.graph_objs as go

app = Flask(__name__)

@app.route('/chart', methods=['POST'])
def create_chart():
    data = request.get_json()
    x = ['Milestone 1', 'Milestone 2', 'Milestone 3', 'Milestone 4']
    y = data['data']
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Data'))
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Trend'))
    fig.update_layout(title='Trend Chart', xaxis_title='Milestones', yaxis_title='Score')
    chart_link = fig.to_html(full_html=False)
    return jsonify({'chart_link': chart_link})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
