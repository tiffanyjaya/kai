import PropTypes from "prop-types";
import React from "react";

class Comment extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return(
            <div className="comment">
                <p className="comment-header">{this.props.author}</p>
                <p className="comment-body">{this.props.message}</p>
                <div className="comemnt-footer">
                    <a href="#" className="comment-footer-delete">Delete comment</a>
                </div>
            </div>
        );
    }

    Contacts.propTypes = {
        author: PropTypes.string,
        message: PropTypes.string
    };

    Contacts.defaultProps = {
        author: "Anonymous",
        message: ""
    };

}
