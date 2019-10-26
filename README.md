# django-http-methods

Middleware to support standard HTTP verbs DELETE and PUT for Django without Django Rest Framework. Also available for add another or custom verbs.

Working on Python 3+ and Django 2+

## Fundamentals

Django, nativelly, doesn't support another HTTP verbs than GET and POST; but it's possible use anothers in a standard way. To do so, it's necessary make a POST request with the header X-HTTP-Method-Override, wich indicates that actual method it's meant to be overrided with the value of the header.

## Usage

1. Add the middleware.py file to your project

2. Add the HttpXMethodOverride to the middlewares list on settings.py
    ```python
    MIDDLEWARE = [
    ... ,
    your_app.middleware.HttpXMethodOverride,
    ]
    ```
3. Access accordingly of the verb:

    ```python
    request.DELETE["some_key"]
    
    # or
    
    request.PUT["some_key"]
    ```

## Examples on making a request on jQuery

```javascript
$.ajax({
    type: 'POST',
    url: some_url,
    beforeSend: function(request)
    {
      request.setRequestHeader('X-Method-Override', 'DELETE') // Can use PUT instead of DELETE
    },
    success: function(data, textStatus, jqXHR)
    {
       console.log(data)
    },
});
```