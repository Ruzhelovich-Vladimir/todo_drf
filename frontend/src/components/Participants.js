import React from 'react'
import {Link} from 'react-router-dom'

const ParticipantItem = ({item}) => {
    return (
        <tr>
            <td>{item.uid}</td>
            <td>{item.firstName}, {item.lastName}</td>
            <td>{item.birthday}</td>
            <td><Link to={`developments/${item.uid}`}>проекты</Link></td>
            <td><Link to={`nodes/${item.uid}`}>задачи</Link></td>
        </tr>
    )
}

const ParticipantList = ({participants}) => {

    return (
        <table border="1" >
            <th>uid</th>
            <th>Участник</th>
            <th>День рождения</th>
            <th>Занят в проектах</th>
            <th>Задачи в проектах</th>
            {participants.map((item) => <ParticipantItem item={item} />)}
        </table>
    )
}

export default ParticipantList