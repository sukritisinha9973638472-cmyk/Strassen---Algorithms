# Matrix-Compute-Service: Strassen Algorithm API

### Overview
Production-ready REST API for matrix multiplication using Strassen's algorithm. Reduces time complexity from O(n³) to O(n^2.81) for large matrices.

### Tech Stack
Python, Flask, NumPy, Docker, Gunicorn

### API Endpoints
**POST** `/multiply` - Multiply two matrices

**Request Body:**
```json
{
  "matrixA": [[1,2],[3,4]],
  "matrixB": [[5,6],[7,8]]
}
