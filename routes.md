url:'http://localhost:8000/v1/'

دقت شود که
Authorization ها
رو تو header http
باید بفرستی

user:{
    create:{
        uri:'users/',
        method:'POST',
        data:{
            username:'username',  //required
            password:'password',    //required
            first_name:'first_name',
            last_name:'lastname',
            email:'email',
            phone:'phone',
            adres:'adres',
            desc:'bio',
            avatar:'image'
        },
        output:{
            id:'user id',
            username:'username',
        }
    },
    login:{
        uri:'users/login/,
        method:'POST',
        data:{
            username:'username',
            password:'password',
        },
        output:{
            id:'user id',
            token:'token string'
        }
    },
    //edit profile
    profile:{
        uri:'users/login/<int:user_id>/',
        method:'PUT',
        data:{
            Authorization:'Token token_string'
        },
        output:{
            user infoes
        }
    },
}


post:{
    create:{
        uri:'posts/',
        method:'POST',
        data:{
            Authorization: 'Token token_string',
            title:'post title',
            content:'post content',
        },
        output:{
            new post
        }
    },
    list:{
        uri:'posts/',
        method:'GET',
        data:{
            Authorization: 'Token token_string',
        },
        output:{
            all user posts
        }
    },
    detail:{
        uri:'posts/<int:post_pk>/',
        Authorization: 'Token token_string',
        output:{
            one user post
        }
    },
}