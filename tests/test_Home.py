def test_inputs(app, client):
   with app.test_client() as test_client:
       res = test_client.get('/')
       assert res.status_code == 200
       assert b"Vertical Tank Maintenance" in res.data 

def test_about(app, client):
   with app.test_client() as test_client:
       res = test_client.get('/about')
       assert res.status_code == 200

def test_estimate(app, client):
   with app.test_client() as test_client:
       res = test_client.get('/estimate')
       assert res.status_code == 200

def test_functionality(app, client):
    print(" -- /result 'estimate_total' POST test")
    with app.test_client() as test_client:
        cost = {"radius": "180", "height": "360"}
        res = test_client.post('/estimate', data=cost)
        assert res.status_code == 200
        assert b"141,300"















#def test_route(app, client):
 #   """
  #  GIVEN a Flask applicatin configured for testing
  #  WHEN the '/' route is requested (GET)
  #  THEN check that the response is valid
  #  """
   # with app.test_client as test_client:
     #   res = test_client.get('/')
      #  assert res.status_code == 200
     #   assert b"Vertical Tank Maintenance" in res.data

#def test_about_route(app, client):
  #  """
  #  GIVEN a Flask applicatin configured for testing
  #  WHEN the '/' route is requested (GET)
  #  THEN check that the response is valid
  #  """
   # with app.test_client as test_client:
    #    res = test_client.get('/about')
    #    assert res.status_code == 200
    #    assert b"About VTM" in res.data

#def test_estimate_route(app, client):
   # """
   # GIVEN a Flask applicatin configured for testing
   # WHEN the '/' route is requested (GET)
  #  THEN check that the response is valid
  #  """
  #  with app.test_client as test_client:
   #     res = test_client.get('/estimate')
   #     assert res.status_code == 200
   #     assert b"Estimate VTM" in res.data

#def test_VTM_route(app, client):
   # """
   # GIVEN a Flask applicatin configured for testing
   # WHEN the '/' route is requested (GET)
   # THEN check that the response is valid
   # """
   # print("\r")
   # print(" -- estimate unit test")
   # with app.test_client as test_client:
   #     estimate = {"radius": "180", "height": "360"}
    #    res = test_client.post('/estimate', data= estimate)
   #     assert res.status_code == 200
   #     assert b"141,300" in res.data

#^ unable to fix "fixture 'app' not found" error

       