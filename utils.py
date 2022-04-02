import json


class DataComments:
    def __init__(self, path_data, path_comments):
        self.path_data = path_data
        self.path_comments = path_comments

    def get_posts_all(self):
        """возвращает посты"""
        with open(self.path_data, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_posts_by_user(self, user_name):
        """возвращает посты определенного пользователя"""
        data_all = self.get_posts_all()
        data_user_all = []
        for data_user in data_all:
            if user_name == data_user["poster_name"]:
                data_user_all.append(data_user)
        return data_user_all

    def get_comments_by_post_id(self, post_id):
        """возвращает комментарии определенного поста"""
        with open(self.path_comments, "r", encoding="utf-8") as file:
            comments_all = json.load(file)
        comments = []
        for comment in comments_all:
            if post_id == comment["post_id"]:
                comments.append(comment)
        return comments

    def search_for_posts(self, query):
        """возвращает список постов по ключевому слову"""
        data_all = self.get_posts_all()
        query_posts = []
        for data in data_all:
            if query.lower() in data["content"].lower():
                query_posts.append(data)
        return query_posts

    def get_post_by_pk(self, pk):
        """возвращает один пост по его идентификатору"""
        data_all = self.get_posts_all()
        for data in data_all:
            if pk == data["pk"]:
                return data

