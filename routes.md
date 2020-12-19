url:'http://localhost:8000/v1/'

هر ایتمی که بالای آن 
login_required
گذاشته باشم. باید در 
http header
مقدار زیر را قرار دهید
Auhtorization: 'Token token_string'

token_string همان مقداری است که در موقع لاگین شدن کاربر از سرور دریافت می شود

user:{
    create:{
        uri:'users/',
        method:'POST',
        send:{
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
        receive:{
            id:'user id',
            username:'username',
            status:201,
            error_status:400,
        }
    },
    login:{
        uri:'users/login/,
        method:'POST',
        send:{
            username:'username',
            password:'password',
        },
        receive:{
            id:'user id',
            token:'token string',
            status:200,
            error_status:400
        }
    },
    //edit profile
    //login_required
    profile:{
        uri:'users/login/<int:user_id>/',
        method:'PUT',
        send:{},
        receive:{
            user infoes
        }
    },
}


post:{
    //login_required
    create:{
        uri:'posts/',
        method:'POST',
        send:{
            title:'post title',
            content:'post content',
        },
        receive:{
            new post
        }
    },
    //login_required
    list:{
        uri:'posts/',
        method:'GET',
        send:{},
        receive:{
            all user posts
        }
    },
    //login_required
    detail:{
        uri:'posts/<int:post_pk>/',
        send:{},
        receive:{
            one user post
        }
    },
}