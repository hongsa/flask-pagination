# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template,flash, session, request,jsonify,g
from sqlalchemy import desc
from apps.models import Rating,User,Lecture
from apps.controller.pagination import pagination
from apps import db


def my_rating(page):

    my_rating = g.user.rating_user.order_by(desc(Rating.joinDATE)).offset((page - 1) * 8).limit(8)
    
    #count total
    total = g.user.rating_user.count()

    #pagination class
    paging = pagination(total,page)
    up = paging.up()
    down = paging.down()
    total_page = paging.totalCount()
    
    return render_template("my_rating.html",my_rating=my_rating, total_page=total_page, up = up, down = down, page=page)