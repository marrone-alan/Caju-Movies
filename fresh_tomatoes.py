import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Caju Movies!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .storyline-div {
            margin: 19px;
        }
        .storyline-title {
            font-size: 19pt;
        }
        .storyline-text {
            font-size: 10pt;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.close, .modal-backdrop', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            var storyline = $(this).attr('data-storyline');
            var title = $(this).attr('data-title');
            var cast = $(this).attr('data-cast');
            var genre = $(this).attr('data-genre');
            var duration = $(this).attr('data-duration');
            
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
            $("#movie-storyline").empty().append($("<p></p>", {
              'id': 'movie-description',
              'class': 'storyline-text'
            }).text(storyline));
            $("#modal-title").empty().text(title);
            $("#movie-cast").empty().text(cast);
            $("#movie-genre").empty().text(genre);
            $("#movie-duration").empty().text(duration);
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer" data-backdrop="static">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">&times;</button>
            <h4 id="modal-title"></h4>
            <div class="subtext">
              <span id="movie-cast"></span>
              <span>|</span>
              <span id="movie-genre"></span>
              <span>|</span>
              <span id="movie-duration"></span>
            </div>
          </div>
          <div class="scale-media" id="trailer-video-container">
          </div>
          <div class="storyline-div">
            <span class="storyline-title">Storyline</span>
            <span id="movie-storyline">
              </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Caju Movies</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# All the information that will be placed on the modal
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center"
     data-title="{movie_title}"
     data-storyline="{movie_storyline}"
     data-trailer-youtube-id="{trailer_youtube_id}"
     data-cast="{movie_cast}"
     data-genre="{movie_genre}"
     data-duration="{movie_duration}"
     data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_storyline=movie.storyline,
            movie_cast=movie.cast,
            movie_genre=movie.genre,
            movie_duration=movie.duration
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
