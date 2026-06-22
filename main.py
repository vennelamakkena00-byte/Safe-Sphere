from fastapi import FastAPI
app=FastAPI(title='SafeSphere AI')

@app.get('/')
def root():
    return {'status':'running'}
