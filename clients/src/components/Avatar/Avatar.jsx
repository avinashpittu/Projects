import React from 'react'

const Avatar = ({children, backgroundColor,px,py,padding,color,borderRadius,fontSize,textAlign,cursor,width,height}) => {
    const style = {
        backgroundColor,
        padding: '${py} ${px}',
        color: color || 'black',
        borderRadius,
        fontSize,
        textAlign: "center",
        cursor: cursor || null,
        textDecoration: "none",
        width,
        height
    }
    // to use this avatar style mutliple places
    return (
    <div style={style}>
      {children}
    </div>
  )
}

export default Avatar
