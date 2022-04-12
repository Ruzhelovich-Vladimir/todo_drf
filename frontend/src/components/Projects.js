import React from 'react'

const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.name}</td>
            <td>{item.repositoryUrl}</td>
            <td>{item.createdAt}</td>
            <td>{item.updatedAt}</td>
        </tr>
    )
}

const ProjectList = ({projects}) => {

    return (
        <table border="1" >
            <th>Наименование</th>
            <th>Репозиторий</th>
            <th>Создан</th>
            <th>Изменён</th>
            {projects.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}

export default ProjectList