import Comment from "./Comment";
import React from "react";

class CommentBox extends React.Component {

    constructor(props) {
        super(props);
    }

    _getComments() {
        const commentList = [
            {id: 1, author: "Morgan McCircuit", message: "Great picture!"},
            {id: 2, author: "Bending Bender", message: "Excellent stuff"}
        ];
        return commentList.map( (comment) => {
            return (
                <Comment author={comment.author} message={comment.message} key={comment.id}/>
            );
         });
    }

    render() {
        const comments = this._getComments();
        return(
            <div className="comment-box">
                <h3>Comments</h3>
                <h4 className="comment-count">{comments.length} comments</h4>
                <div className="comemnt-list">
                    {comments}
                </div>
            </div>
        );
    }

}
