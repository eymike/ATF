﻿//Copyright © 2014 Sony Computer Entertainment America LLC. See License.txt.

using System;

namespace Sce.Atf
{
    /// <summary>
    /// Interface for resources that have a type and unique resource identifier (URI)</summary>
    public interface IResource
    {
        /// <summary>
        /// Gets a string identifying the type of the resource to the end-user</summary>
        string Type
        {
            get;
        }

        /// <summary>
        /// Gets or sets the resource URI. It should be an absolute path. (Uri.IsAbsoluteUri should be true.)</summary>
        Uri Uri
        {
            get;
            set;
        }

        /// <summary>
        /// Event that is raised after the resource's URI changes</summary>
        event EventHandler<UriChangedEventArgs> UriChanged;
    }

    public static class Resource
    {
        /// <summary>
        /// Gets a local operating system representation of this resource's URI</summary>
        /// <returns>Uri.LocalPath</returns>
        public static string GetPathName(this IResource resource)
        {
            return resource.Uri.LocalPath;
        }
    }

}
