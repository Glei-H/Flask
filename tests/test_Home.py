def test_inputs(app, client):
   with app.test_client() as test_client:
       res = test_client.get('/')
       assert res.status_code == 200
       #assert b"Service Area" in res.data 

def test_about(app, client):
   with app.test_client() as test_client:
       res = test_client.get('/about')
       assert res.status_code == 200

def test_estimate(app, client):
   with app.test_client() as test_client:
       res = test_client.get('/estimate')
       assert res.status_code == 200)
       