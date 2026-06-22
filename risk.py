from fastapi import APIRouter
router=APIRouter()
@router.get('/risk-score')
def risk():
    return {'risk_score':78}
