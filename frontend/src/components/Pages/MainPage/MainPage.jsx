import React from "react";
import { NavLink } from "react-router-dom";
import s from './MainPage.module.scss'

export const MainPage = () => {
    return (
        <div className={s.wrapper}>
            <div className={s.imgcontent}>
                <div className={s.text}>Оставьте все <br />заботы нам</div>
                <div className={s.textin}>
                    <div>
                        <input className={s.input} type="text" />
                    </div>
                    <div className={s.input}>Кнопка</div>
                </div>
            </div>
        </div>
    )
}