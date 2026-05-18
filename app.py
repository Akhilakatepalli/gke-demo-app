from flask import Flask, jsonify

app = Flask(__name__)

claims = [
    {"claim_id": "CLM001", "member": "John Smith", "state": "CA", "amount": 285.00, "status": "APPROVED"},
    {"claim_id": "CLM002", "member": "Maria Garcia", "state": "TX", "amount": 150.00, "status": "DENIED"},
    {"claim_id": "CLM003", "member": "David Lee", "state": "NY", "amount": 500.00, "status": "FRAUD_BLOCKED"},
    {"claim_id": "CLM004", "member": "Sarah Johnson", "state": "FL", "amount": 320.00, "status": "APPROVED"},
    {"claim_id": "CLM005", "member": "James Wilson", "state": "OH", "amount": 195.00, "status": "APPROVED"},
]

@app.route("/")
def home():
    return jsonify({"app": "Healthcare Claims Demo", "version": "1.0", "total_claims": len(claims)})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/claims")
def get_claims():
    return jsonify({"claims": claims, "total": len(claims)})

@app.route("/claims/<claim_id>")
def get_claim(claim_id):
    claim = next((c for c in claims if c["claim_id"] == claim_id), None)
    if not claim:
        return jsonify({"error": "Claim not found"}), 404
    return jsonify(claim)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
