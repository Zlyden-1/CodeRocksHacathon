import React from "react";
import { NavLink } from "react-router-dom";
import s from './Footer.module.scss'

export const Footer = () => {
    return (
        <div className={s.wrapper}>
            <div className={s.header}>
                <img src="./SKILLMATCH.svg" />
                <div className={s.menu}>
                    <div className={s.leftmenu}>
                        <NavLink to='/'>Новый заказ</NavLink>
                        <NavLink to='/'>Все услуги</NavLink>
                        <NavLink to='/lk'>История заказов</NavLink>
                    </div>
                    <div className={s.leftmenu}>
                        <NavLink to='/auth'>Вход для специалистов</NavLink>
                        <NavLink to='/auth'>Вход для исполнителей</NavLink>
                    </div>
                    <div className={s.leftmenu}>
                        <div>Служба поддержки</div>
                        <div>+8 (927) 456-32-45</div>
                    </div>
                </div>
            </div>
        </div>
    )
}