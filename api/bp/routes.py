from flask import Blueprint, jsonify, request
from music_queue import playlist
from errors import BadRequest, MethodNotAllowed
from skip import votetoskip


#: the Flask Blueprint object with route prefix.
api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/submit")
def submit():
    """Submit a song link to the queue.

    ::

      /submit?song=<song_url>

    :param str song_url: The URL of the song
    :return: {"Added": <song_url> }
    :rtype: json
    """
    if "song" not in request.args:
        raise BadRequest
    song = request.args.get("song")
    playlist(song)
    return jsonify({"Added": song})


@api.route("/next")
def up_next():
    """
    provide a route to pop next song from queue.  This route should only be
    used by the Player, in order to get the link for the next track to play.
    Once this route has been called, the item it pops is gone from the queue.

    ::

      /next

    :return: { "Nect": <song_url> }
    :rtype: json

    """
    votetoskip.reset()
    return jsonify({"Next": playlist.next()})


@api.route("/stat")
def stat():
    """
    Returns the length of the playist.

    ::

      /stat

    :return: { "QueueLen": int }
    :rtype: json

    """
    return jsonify({"QueueLen": len(playlist)})


@api.route("/queue")
def queue():
    """
    provides the song queue as a dictionary

    ::

      /queue

    :return: a list of song URLs
    :rtype: List[str]

    """
    return jsonify(list(playlist))


@api.route("/clear")
def clear():
    """
    provides a route to clear the queue.  This route shouldn't be publicly
    exposed, otherwise users will be repeatedly clear the queue of songs.

    ::

      /clear

    :return: { "Cleared": "playlist" }
    :rtype: json

    """
    playlist.clear()
    return jsonify({"Cleared": "playlist"})


@api.route("/current")
def np():
    """
    Returns the song currently playing in the queue.  This

    ::

      /current

    :return: { "Current": <song_url> }
    :rtype: json

    """
    return jsonify({"Current": playlist.current_song})


@api.route("/skip")
def skip():
    """
    Elects to skip the current song.  Will return an error if a username
    is submitted more than once.

    ::

      /skip?username=<user>

    :param str username: The name of the user requesting a skip.
    :return: { "Skip": "200" }
    :rtype: json
    :raises: MethodNotAllowed

    .. todo:: remove status code from body of response
    """
    if playlist.current_song is None:
        raise MethodNotAllowed

    votetoskip(request.args.get("username"), request.remote_addr)
    return jsonify({"Skip": "200"})


@api.teardown_app_request
def app_request_teardown(error=None):
    """
    Called after every request.  If there are any errors that were not handled
    during the lifetime of the request, they are raised here.

    :param Exception error: The unhandled Exception
    :return: body of Exception message
    :rtype: str
    """
    if error is not None:
        print([str(_) for _ in error.args])
