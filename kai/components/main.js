import React from "react";
import ReactDom from "react-dom";

class Main extends React.Component {
    render() {
        const now = new Date();
        const topicsList = ["HTML", "Javascript", "React"]
        return(
            <div>
                <h3>Stories App</h3>
                <p classname="lead">Current time: { now.toString() }</p>
                <ul> {topicsList.map( topic => <li>{topic}</li> )}</ul>
            </div>
        );
    }
}

ReactDom.render(<Main />, document.getElementById("kai"))

