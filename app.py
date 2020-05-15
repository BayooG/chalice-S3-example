from chalice import Chalice, Response
from upload import save_img

app = Chalice(app_name='ServiceOfTheWeek-s3-api')
app.debug = True



@app.route('/', )
def index():
    return {'hello': 'world'}

@app.route('/post_img',cors=True, methods=['POST'])
def store():
    try:
        request = app.current_request
        body = app.current_request.json_body
        img = body['img']
        url = save_img(img)      
        if url:
            return Response(status_code=200,body={
                'msg': 'saved',
                'url': url
            })

    except Exception as e:
        return Response(status_code=404,body={
            'msg': 'failed'
        })