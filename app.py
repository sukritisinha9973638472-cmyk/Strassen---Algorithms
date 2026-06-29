from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

def strassen(A, B):
    n = len(A)
    if n <= 64:
        return np.dot(A, B)
    mid = n // 2
    A11, A12 = A[:mid, :mid], A[:mid, mid:]
    A21, A22 = A[mid:, :mid], A[mid:, mid:]
    B11, B12 = B[:mid, :mid], B[:mid, mid:]
    B21, B22 = B[mid:, :mid], B[mid:, mid:]
    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6
    return np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.json
    A = np.array(data['matrixA'])
    B = np.array(data['matrixB'])
    result = strassen(A, B)
    return jsonify({"result": result.tolist()})

@app.route('/health')
def health():
    return "Matrix Service Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
