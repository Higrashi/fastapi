# @app.get('/posts')
# def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     posts = cursor.fetchall()
#     return {"data": posts}

# @app.post('/posts', status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s,%s,%s) RETURNING * """,
#     (post.title, post.content,post.published))
    
#     new_post = cursor.fetchone()
#     conn.commit()
#     return {"data": new_post}

# @app.get('/posts/{id}')
# def get_post(id: int, response: Response):
#     cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
#     post = cursor.fetchone()
    
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#         detail={"message": f"post {id} not found"})
   
#     return {"post_detail": post}

# @app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))
#     deleted_post = cursor.fetchone()
#     conn.commit()
#     if deleted_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} not found") 
    
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put('/posts/{id}')
# def update_post(id: int, post: Post):
#    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
#    (post.title, post.content, post.published, str(id)))
#    updated_post = cursor.fetchone()

#    conn.commit()
#    if updated_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} not found") 
    
#    return {"data": updated_post}
