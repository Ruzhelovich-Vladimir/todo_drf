import React from 'react'
import { useParams } from 'react-router-dom'

const NoteItem = ({item}) => {
    return (
        <tr>
            <td>{item.project.name}</td>
            <td>{item.author.firstName}, {item.author.lastName}</td>
            <td>{item.text}</td>
            <td>{item.status}</td>
            <td>{item.createdAt}</td>
            <td>{item.updatedAt}</td>

        </tr>
    )
}

const NoteList = ({notes}) => {

    let { id } = useParams();
    let filtered_items = id ? notes.filter((item) => item.author.uid == id) : notes

    return (
        <table border="1" >
            <th>Наименование</th>
            <th>Автор</th>
            <th>Текст</th>
            <th>Статус</th>
            <th>Создан</th>
            <th>Изменён</th>
            {filtered_items.map((item) => <NoteItem item={item} />)}
        </table>
    )
}

export default NoteList