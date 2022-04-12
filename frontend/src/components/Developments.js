import React from 'react'
import { useParams } from 'react-router-dom'

const Item = ({item}) => {
    return (
        <tr>
            <td>{item.development.firstName}, {item.development.lastName}</td>
            <td>{item.development.birthday}</td>
            <td>{item.project.name}</td>
            <td>{item.project.projectManager.firstName}, {item.project.projectManager.lastName}</td>
        </tr>
    )
}

const DevelopmentList = ({developments}) => {

    let { id } = useParams();

    let filtered_items = id ? developments.filter((item) => item.development.uid == id): developments

    return (
        <table border="1" >
            <th>Разработчик</th>
            <th>День рождение разработчика</th>
            <th>Наименование проекта</th>
            <th>Проектный менеджер</th>
            {filtered_items.map((item) => <Item item={item} />)}
        </table>
    )
}

export default DevelopmentList