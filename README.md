# *turbo_flask*
trying to figure out how to get Hotwire's (basecamp) TURBO into a flask app. Heavily inspired by the [turbo-rails](https://github.com/hotwired/turbo-rails) gem.

## Implementation Status:
- [ ] Turbo Drive 
- [ ] Turbo Frames
- [ ] Turbo Streams

## Installing Turbo into a flask app
import the turbo_flask folder (using pip eventually lol), then at the top of you main python file:

```py
app = Flask(__name__)
turbo = tf.Turbo(app)
```

then in your `<head>` html tag in your templates:

```html
<head>
    <title>cool app</title>
    <!-- ... --> 

    {{ turbo_js() }}
</head>
```

### TODO
- [ ] get it to auto install the js files

## Turbo Drive
Turbo Drive is enabled by default. You don't have to do anything else. For more info on using Turbo Drive, see the [official turbo page](https://turbo.hotwire.dev/handbook/drive).

**The custom progress bar is enabled by default.** It appears automatically for any page that takes longer than 500ms to load.

### TODO
- [ ] let user set custom progress bar delay.
- [ ] figure out how to add a tag that injects the `turbo-cache-control` meta tag into the head.

## Turbo Frames

## Turbo Streams


---
  
####  ❤️ Thanks
  
Written by [@ehne](https://github.com/ehne) in 2021.  Give this project a star if you found it helpful. 
  
---
[![CodeFactor](https://www.codefactor.io/repository/github/ehne/turbo-flask/badge/main )](https://www.codefactor.io/repository/github/ehne/turbo-flask/overview/main) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ehne/turbo-flask ) [![GitHub issues](https://img.shields.io/github/issues-raw/ehne/graphX )](https://github.com/ehne/turbo-flask/issues)