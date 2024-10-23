from pydantic import BaseModel
from enum import Enum
from datetime import date 


class Roles(str, Enum):
    admin = "administrador"
    editor = "editor"
    lector = "lector"

class UserRegister(BaseModel):
    username: str
    password: str
    email: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserId(BaseModel):
    id: int

class UserName(BaseModel):
    username: str

class User(BaseModel):
    id: int
    username: str
    password: str
    role: Roles

class Login(BaseModel):
    username: str
    password: str

class TravelRegister(BaseModel):
    user_id: int
    trip_name: str
    description: str
    places_visited: list

class DestinyRegister(BaseModel):
    user_id: int
    destiny_name: str
    description: str
    country: str 
    city: str 
    images: list 


class WishlistRegister(BaseModel):
    user_id: int
    list_name: str
    destinies: list

class WishlistFollow(BaseModel):
    user_id: int
    wishlist_id: str 

class WishlistDestiny(BaseModel):
    user_id: int
    wishlist_id: str 
    destiny_id: str

class Reaccion(Enum):
    me_gusta = "me gusta"
    me_encanta = "me encanta"
    me_enamora = "me enamora"
    me_asombra = "me asombra"
    me_entristece = "me entristece"
    me_enoja = "me enoja"

class Likes(BaseModel):
    react_id: int
    user_id: int
    reaccion: Reaccion

class Comment(BaseModel):
    coment_id: int
    user_id: int
    coment_text: str
    reacciones: list

class Post(BaseModel):
    post_id: int
    user_id: int
    text: str
    images: list
    comentarios: list
    reacciones: list

class PostRequest(BaseModel):
    user_id: int
    text: str
    images: list

class CommentRequest(BaseModel):
    user_id: int
    coment_text: str

    
