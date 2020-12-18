url='http://localhost:8000/'

user:
{
    create new user:
    {
        uri:'users/',
        method:'POST',
        data:{
                'username':'myname',
                'password':'mypass',
                'email':'mymail',
                'first_name':'my fname',
                'last_name':'my lname',
                'phone':'myphone',
                'adres':'my address',
                'desc':'my bio',
                'avatar':'my image url',
            }
    },
    login:
    {
        uri:'users/login/',
        method:'POST',
        data:
        {
            username:'username',
            password:'password'
        }
        output:
        {
            token:'token string'
        }
    },
    edit profile:
    {
        header:
        {
            Authorization: 'Token token string'
        }
        uri:'users/login/<int:id>/',
        method:'PUT',
        data:{
                email:'mymail',
                first_name:'my fname',
                last_name:'my lname',
                phone:'myphone',
                adres:'my address',
                desc:'my bio',
                avatar:'my image url',
            }
    },
}

post:
{
    all posts by a user:
    {
        header:
        {
            Authorization: 'Token token string',
        },
        uri:'posts/list/',
        method:'GET',
    },
    post details:
    {
        header:
        {
            Authorization: 'Token token string',
        },
        uri:'posts/list/<int:pk>/
        method:'GET'
    },
}




