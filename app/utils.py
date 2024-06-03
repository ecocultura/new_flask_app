from app.models import Like

def user_liked_posts(user_id, post_id):
    return Like.query.filter_by(user_id=user_id, post_id=post_id).first() is not None
