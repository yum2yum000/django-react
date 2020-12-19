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
            success: user infoes
            status:201,
            error_status:400,406,
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
        send:{
            update:'password','data', None
            در صورتی که پسورد ارسال کنید، درخواست تغییر پسورد داده اید. و در صورتی که دیتا ارسال
            کنید درخواست تغییر چیزهایی به غیر از پسورد داده اید. 
            و در صورتی که خالی ارسال کنید، اطلاعات فعلی یوزر را درخواست کرده اید.

            username 
            last_login
            date_joined
            غیر قابل تغییر می باشند
        },
        receive:{
            user infoes
            status:200,
            error_status=400, 403
        }
    },
}


post:{
    all_posts:{
        uri:'posts/',
        method:'GET',
        send:{},
        receive:{
            all posts 
        },
        status:200,
    },

    //login_required
    create:{
        uri:'posts/<user_id>/',
        method:'POST',
        send:{
            title:'post title', //required
            content:'post content', //required
        },
        receive:{
            new post
        },
        status: 200,
    },
    //login_required
    list:{
        //لیست کردن پست های یک یوزر خاص
        uri:'posts/<user_id>/',
        method:'GET',
        send:{},
        receive:{
            all user posts
        },
        status: 200,
        err_status: 404
    },
    //login_required
    one_post:{
        //گرفتن یک پست از یک یوزر خاص
        uri:'posts/<user_id>/<post_pk>/',
        method:'GET',
        send:{},
        receive:{
            one user post
        },
        status: 201,
        err_status: 400
    },
    //login_required
    update:{
        uri:'posts/<user_id>/<post_pk>/',
        method:'PUT',
        send:{
            title:'new title',
            content:'new content'
        },
        receive:{
            new post
        },
        status: 200,
        err_status: 400
    },
    DELETE:{
        uri:'posts/<user_id>/<post_pk>/',
        method:'DELETE',
        send:{}
        recevive:{
            'post':'deleted'
        },
        status: 200,
        err_status: 400
    }
}