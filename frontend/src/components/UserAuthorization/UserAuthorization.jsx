import React from "react";
import { NavLink } from "react-router-dom";
import s from './UserAuthorization.module.scss'
import axios from "axios";

export class UserAuthorization extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            login: "",
            password: "",
        };
    }

    handleSubmit = (event) => {
        event.preventDefault();

        const data = {
            login: this.state.login,
            password: this.state.password,
        };

        axios.post('http://95.163.240.234:8000/', data)
            .then(response => {
                console.log(response);
                // Дальнейшая обработка ответа от сервера
            })
            .catch(error => {
                console.log(error);
                // Обработка ошибок, возникших при отправке запроса
            });
    }

    render() {
        return (
            <div className={s.wrapper}>
                <div className={s.wrapperhead}>
                    <NavLink to='/auth'style={{ backgroundColor: '#D24C00'}}>Вход</NavLink>
                    <NavLink to='/reg'>Регистрация исполнителя</NavLink>
                </div>
                <form className={s.form} onSubmit={this.handleSubmit}>
                    <input className={s.component} placeholder="Логин" onChange={(e) => this.setState({ login: e.target.value })} />
                    <input className={s.component} placeholder="Пароль" onChange={(e) => this.setState({ password: e.target.value })} />
                    <button style={{ marginTop: '20px' }} className={s.component} type="submit">Вход</button>
                </form>
            </div>
        )
    }
}