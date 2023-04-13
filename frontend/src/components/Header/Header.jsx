import React from "react";
import { NavLink } from "react-router-dom";
import s from './Header.module.scss'

export const Header = () => {
    return (
        <div className={s.wrapper}>
            <div className={s.header}>
                <img src="./SKILLMATCH.svg" />
                <div className={s.menu}>
                    <NavLink to='/'>Главная</NavLink>
                    <NavLink to='/'>Специалисту</NavLink>
                    <NavLink to='/auth'>Вход</NavLink>
                </div>
            </div>
        </div>
    )
}