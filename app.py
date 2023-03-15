from flask import Flask, request, jsonify
from py2neo import Graph
import json

app = Flask(__name__)
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

@app.route('/events', methods=['GET'])
def get_events():
    name = request.args.get('name')
    query = '''
    MATCH (p:Person)<-[:PARTICIPATED_IN]->(e:Event)
    WHERE p.name = $name
    RETURN e.id AS id
    '''
    result = graph.run(query, name=name).data()
    events = [r['id'] for r in result]
    response = {'events': events, 'name': name}
    return json.dumps(response, ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)