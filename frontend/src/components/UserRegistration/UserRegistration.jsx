import React from "react";
import { NavLink } from "react-router-dom";
import s from './UserRegistration.module.scss'
import axios from "axios";

export class UserRegistration extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            surname: "",
            name: "",
            patronymic: "",
            login: "",
            email: "",
            telephone: "",
            password: "",
            enterpassword: ""
        };
    }

    handleSubmit = (event) => {
        event.preventDefault();

        const data = {
            surname: this.state.surname,
            name: this.state.name,
            patronymic: this.state.patronymic,
            email: this.state.email,
            telephone: this.state.telephone,
            password: this.state.password,
            enterpassword: this.state.enterpassword
        };

        axios.post('http://95.163.240.234:8000/rgstr_user', data)
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
                    <NavLink to='/reg' style={{ backgroundColor: '#D24C00' }}>Регистрация исполнителя</NavLink>
                    <NavLink to='/auth'>Вход</NavLink>
                </div>
                <form className={s.form} onSubmit={this.handleSubmit}>
                    <input className={s.component} required placeholder="Фамилия" onChange={(e) => this.setState({ surname: e.target.value })} />
                    <input className={s.component} required placeholder="Имя" onChange={(e) => this.setState({ name: e.target.value })} />
                    <input className={s.component} required placeholder="Отчество" onChange={(e) => this.setState({ patronymic: e.target.value })} />
                    <input className={s.component} required type="email" placeholder="Электронная почта" onChange={(e) => this.setState({ email: e.target.value })} />
                    <input className={s.component} required placeholder="Номер телефона" onChange={(e) => this.setState({ telephone: e.target.value })} />
                    <input className={s.component} required placeholder="Пароль" onChange={(e) => this.setState({ password: e.target.value })} />
                    <input className={s.component} required placeholder="Подтверждение пароля" onChange={(e) => this.setState({ enterpassword: e.target.value })} />
                    <button style={{ marginTop: '20px' }} className={s.component} type="submit">Завершить регистрацию</button>
                </form>
            </div>
        )
    }
}