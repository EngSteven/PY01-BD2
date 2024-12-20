from fastapi import APIRouter, Depends
from models.schemas import *
from mongo_data import DatabaseMongo  
from auth import * 
from bson import ObjectId

router = APIRouter()
db = DatabaseMongo()

"""
--------------------------------------------------
POSTS
--------------------------------------------------
"""

@router.get("/posts")
async def get_posts():
    res = db.get_all_posts()    
    return {"Posts recientes": res}

@router.post("/{user_id}/posts/post")
async def insert_post(user_id: int, post: PostRequest): #Sirve
    post_data = PostRequest(
        text = post.text,
        images = post.images,
    )
    res = db.insert_post(user_id, post_data)
    return {"Post ingresado": res}

@router.get("/{user_id}/posts")
async def get_posts(user_id: int):
    res = db.get_user_posts(user_id)    
    return {"Posts recientes": res}

@router.get("/{user_id}/posts/{post_id}")
async def get_post(post_id: str):
    res = db.get_post_from_post(ObjectId(post_id)) 
    return {"Post": res}

@router.put("/{user_id}/posts/{post_id}/update")
async def update_post(post_id: str, post: PostUpdateRequest):  
    post_data = PostUpdateRequest(
        text = post.text
    )
    res = db.set_post(post_id, post_data)
    return {"Post actualizado": res}

@router.delete("/{user_id}/posts/{post_id}/delete")
async def delete_post(post_id: str):
    return {db.delete_post(post_id)}

"""
--------------------------------------------------
COMMENTS
--------------------------------------------------
"""

### ** PARA POSTS **

@router.post("/{user_id}/posts/{post_id}/comment")
async def post_comment(user_id: int, post_id: str, comment: CommentRequest):
    post_data = CommentRequest(
        coment_text = comment.coment_text
    )
    res = db.add_comment_to_post(user_id, post_id, post_data)
    print("Comentario: ", res)
    return{"Comentario" : res}

@router.get("/{user_id}/posts/{post_id}/comment/{comment_id}")
async def get_comment(comment_id: str):
    res = db.get_comment_from_post(comment_id)
    print("Comentario:", res)
    return {"Comentario": res}

@router.get("/{user_id}/posts/{post_id}/comments/all")
async def get_comment(post_id: str):
    res = db.get_all_comments_from_post(post_id)
    print("Comentario:", res)
    return {"Comentarios": res}

@router.put("/{user_id}/posts/{post_id}/comment/{comment_id}/update")
async def update_comment(comment_id: str, comment: CommentUpdateRequest):
    post_data = CommentUpdateRequest(
        coment_text = comment.coment_text
    )
    res = db.set_comment_from_post(comment_id, post_data)
    print("Post: ", res)
    return {"Post actualizado": res}

@router.delete("/{user_id}/posts/{post_id}/comment/{comment_id}/delete")
async def delete_comment(post_id: str, comment_id: str): 
    db.remove_comment_from_post(post_id, comment_id)
    return {"Comentario eliminado exitosamente"}


### ** PARA DESTINIES **

@router.post("/{user_id}/destinies/{destiny_id}/comment")
async def post_comment(user_id: int, destiny_id: str, comment: CommentRequest):
    destiny_data = CommentRequest(
        coment_text = comment.coment_text
    )
    res = db.add_comment_to_destiny(user_id, destiny_id, destiny_data)
    print("Comentario: ", res)
    return{"Comentario" : res}

@router.get("/{user_id}/destinies/{destiny_id}/comment/{comment_id}")
async def get_comment(comment_id: str):
    res = db.get_comment_from_destiny(comment_id)
    print("Comentario:", res)
    return {"Comentario": res}

@router.get("/{user_id}/destinies/{destiny_id}/comments/all")
async def get_comment(destiny_id: str):
    res = db.get_all_comments_from_destiny(destiny_id)
    print("Comentario:", res)
    return {"Comentarios": res}

@router.put("/{user_id}/destinies/{destiny_id}/comment/{comment_id}/update")
async def update_comment(comment_id: str, comment: CommentUpdateRequest):
    destiny_data = CommentUpdateRequest(
        coment_text = comment.coment_text
    )
    res = db.set_comment_from_destiny(comment_id, destiny_data)
    print("Destiny: ", res)
    return {"Destiny actualizado": res}

@router.delete("/{user_id}/destinies/{destiny_id}/comment/{comment_id}/delete")
async def delete_comment(destiny_id: str, comment_id: str): 
    db.remove_comment_from_destiny(destiny_id, comment_id)
    return {"Comentario eliminado exitosamente"}


"""
--------------------------------------------------
REACTIONS
--------------------------------------------------
"""

### ** PARA POSTS **

@router.post("/{user_id}/posts/{post_id}/react")
async def post_reaction(user_id: int, post_id: str, reaccion: LikesRequest):
    post_data = LikesRequest(
        reaccion = reaccion.reaccion
    )
    res = db.add_reaction_to_post(user_id, post_id, post_data)
    print("Reaccion: ", res)
    return{"Reaccion" : res}

@router.get("/{user_id}/posts/{post_id}/reaction/{reaction_id}")
async def get_reaction(reaction_id: str):
    res = db.get_reaction_from_post(reaction_id)
    print("Reaccion:", res)
    return {"Reaccion": res}

@router.get("/{user_id}/posts/{post_id}/reactions/all")
async def get_comment(post_id: str):
    res = db.get_all_reactions_from_post(post_id)
    return {"Reacciones": res}

@router.put("/{user_id}/posts/{post_id}/reaction/{reaction_id}/update")
async def update_reaction(reaction_id: str, reaccion: LikesUpdateRequest):
    post_data = LikesUpdateRequest(
        reaccion = reaccion.reaccion
    )
    res = db.set_reaction_from_post(reaction_id, post_data)
    print("Reaccion: ", res)
    return {"Reaccion actualizada": res}

@router.delete("/{user_id}/posts/{post_id}/reaction/{reaction_id}/delete")
async def delete_reaction(post_id: str, reaction_id: str):
    res = db.remove_reaction_from_post(post_id, reaction_id)
    return {res}

### ** PARA DESTINIES **

@router.post("/{user_id}/destinies/{destiny_id}/react")
async def post_reaction(user_id: int, destiny_id: str, reaccion: LikesRequest):
    destiny_data = LikesRequest(
        reaccion = reaccion.reaccion
    )
    res = db.add_reaction_to_destiny(user_id, destiny_id, destiny_data)
    print("Reaccion: ", res)
    return{"Reaccion" : res}

@router.get("/{user_id}/destinies/{destiny_id}/reaction/{reaction_id}")
async def get_reaction(reaction_id: str):
    res = db.get_reaction_from_destiny(reaction_id)
    print("Reaccion:", res)
    return {"Reaccion": res}

@router.get("/{user_id}/destinies/{destiny_id}/reactions/all")
async def get_comment(destiny_id: str):
    res = db.get_all_reactions_from_destiny(destiny_id)
    return {"Reacciones": res}

@router.put("/{user_id}/destinies/{destiny_id}/reaction/{reaction_id}/update")
async def update_reaction(reaction_id: str, reaccion: LikesUpdateRequest):
    destiny_data = LikesUpdateRequest(
        reaccion = reaccion.reaccion
    )
    res = db.set_reaction_from_destiny(reaction_id, destiny_data)
    print("Reaccion: ", res)
    return {"Reaccion actualizada": res}

@router.delete("/{user_id}/destinies/{destiny_id}/reaction/{reaction_id}/delete")
async def delete_reaction(destiny_id: str, reaction_id: str):
    res = db.remove_reaction_from_destiny(destiny_id, reaction_id)
    return {res}

### ** PARA COMENTARIOS **

@router.post("/{user_id}/comments/{comment_id}/react")
async def post_reaction(user_id: int, comment_id: str, reaccion: LikesRequest):
    destiny_data = LikesRequest(
        reaccion = reaccion.reaccion
    )
    res = db.add_reaction_to_comment(user_id, comment_id, destiny_data)
    print("Reaccion: ", res)
    return{"Reaccion" : res}

@router.get("/{user_id}/comments/{comment_id}/reaction/{reaction_id}")
async def get_reaction(reaction_id: str):
    res = db.get_reaction_from_comment(reaction_id)
    print("Reaccion:", res)
    return {"Reaccion": res}

@router.get("/{user_id}/comments/{comment_id}/reactions/all")
async def get_comment(comment_id: str):
    res = db.get_all_reactions_from_comment(comment_id)
    return {"Reacciones": res}

@router.put("/{user_id}/comments/{comment_id}/reaction/{reaction_id}/update")
async def update_reaction(reaction_id: str, reaccion: LikesUpdateRequest):
    comment_data = LikesUpdateRequest(
        reaccion = reaccion.reaccion
    )
    res = db.set_reaction_from_comment(reaction_id, comment_data)
    print("Reaccion: ", res)
    return {"Reaccion actualizada": res}

@router.delete("/{user_id}/comments/{comment_id}/reaction/{reaction_id}/delete")
async def delete_reaction(comment_id: str, reaction_id: str):
    res = db.remove_reaction_from_comment(comment_id, reaction_id)
    return {res}

@router.get("/{user_id}/top_comments")
async def top_comments():
    res = db.get_top_comment_posts(5)
    return{"Top comentarios": res}
