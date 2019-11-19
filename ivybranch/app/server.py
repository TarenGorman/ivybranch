from flask import Flask, request, jsonify, render_template
import ivybranch.core as ivy

server = Flask("ivy")

@server.route("/api/linear/<size>")
def get_linear(size):
    l = ivy.linear.LinkedList()
    return jsonify(l.__repr__())

@server.route("/api/map/<size>")
def get_map(size):
    m = ivy.map.Hashmap()
    return jsonify(m.__repr__())

@server.route("/api/tree/<size>")
def get_tree(size):
    t = ivy.tree.BinaryTree("a")
    return jsonify(t.__repr__())

@server.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    server.run(debug=True)
