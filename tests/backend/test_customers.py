def test_create_and_get_customer(client):
    create_response = client.post(
        "/api/v1/customers",
        json={"full_name": "Ada Lovelace", "email": "ada@example.com"},
    )
    assert create_response.status_code == 201
    customer = create_response.json()
    assert customer["email"] == "ada@example.com"

    get_response = client.get(f"/api/v1/customers/{customer['id']}")
    assert get_response.status_code == 200
    assert get_response.json()["full_name"] == "Ada Lovelace"


def test_get_missing_customer_returns_404(client):
    response = client.get("/api/v1/customers/does-not-exist")
    assert response.status_code == 404
